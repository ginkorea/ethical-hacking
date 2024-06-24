from scapy.all import ARP, Ether, srp, ICMP, IP, sr1, TCP, conf
import sys
import os


def arp_scan(ip):
    # Create ARP request packet
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Send packet and capture the response
    result = srp(packet, timeout=2, verbose=False)[0]

    # Parse the response
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices


def ping_scan(ip):
    # Create ICMP ping request
    icmp = IP(dst=ip) / ICMP()

    # Send the packet and capture the response
    response = sr1(icmp, timeout=2, verbose=False)

    if response:
        return True
    else:
        return False


def tcp_scan(ip, port=8080):
    # Create TCP SYN packet
    syn = IP(dst=ip) / TCP(dport=port, flags="S")

    # Send the packet and capture the response
    response = sr1(syn, timeout=2, verbose=False)

    if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
        # Send RST packet to close the connection
        rst = IP(dst=ip) / TCP(dport=port, flags="R")
        sr1(rst, timeout=2, verbose=False)
        return True
    else:
        return False


def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=5, verbose=False)[0]
    if answered_list:
        return answered_list[0][1].hwsrc
    return None


def traceroute_to(ip):
    # Use scapy's traceroute function to see the path
    conf.verb = 0  # Disable verbose output
    result, _ = srp(IP(dst=ip, ttl=(1, 30)) / ICMP(), timeout=2)
    hops = []
    for _, received in result:
        hops.append(received.src)
    return hops


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 network_scan.py <IP>")
        sys.exit(1)

    ip = sys.argv[1]

    print(f"Scanning {ip}...")

    # Step 1: ICMP Ping Scan
    if ping_scan(ip):
        print(f"Host {ip} is up (ICMP Ping).")
    else:
        print(f"Host {ip} did not respond to ICMP Ping.")

    # Step 2: TCP Syn Scan on Port 80
    if tcp_scan(ip):
        print(f"Host {ip} is up (TCP Port 8080).")
    else:
        print(f"Host {ip} did not respond on TCP Port 8080.")

    # Step 3: ARP Scan
    devices = arp_scan(ip)
    if devices:
        print("Available devices in the network:")
        print("IP" + " " * 18 + "MAC")
        for device in devices:
            print("{:16}    {}".format(device['ip'], device['mac']))
    else:
        print("No devices found with ARP scan.")

    # Step 4: Get MAC Address of Specific IP
    mac = get_mac(ip)
    if mac:
        print(f"MAC address of {ip} is {mac}")
    else:
        print(f"Could not resolve MAC address for {ip}")

    # Step 5: Traceroute to the IP
    print(f"Performing traceroute to {ip}...")
    hops = traceroute_to(ip)
    print(f"Traceroute result: {' -> '.join(hops)}")

    if len(hops) > 1:
        # Attempt ARP on the last hop before the destination
        last_hop = hops[-2]
        mac = get_mac(last_hop)
        if mac:
            print(f"MAC address of last hop {last_hop} is {mac}")
        else:
            print(f"Could not resolve MAC address for last hop {last_hop}")
