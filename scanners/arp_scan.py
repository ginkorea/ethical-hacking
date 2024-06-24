from scapy.all import ARP, Ether, srp
import sys


def arp_scan(ip_range, debug=True):
    # Create ARP request packet
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Send packet and capture the response
    result = srp(packet, timeout=2, verbose=False)[0]
    if debug:
        print(result)

    # Parse the response
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 arp_scan.py <IP_RANGE>")
        sys.exit(1)

    ip_range = sys.argv[1]
    devices = arp_scan(ip_range)
    print("Available devices in the network:")
    print("IP" + " " * 18 + "MAC")
    for device in devices:
        print("{:16}    {}".format(device['ip'], device['mac']))
