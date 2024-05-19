import subprocess
import re
import random
import argparse


class MacSpoofer:
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


def main():
    parser = argparse.ArgumentParser(description='MAC Address Spoofer')
    parser.add_argument('-i', '--interface', help='Network interface to spoof (default: all)')
    parser.add_argument('-m', '--manufacturer', choices=MacSpoofer.manufacturers.keys(),
                        help='Manufacturer for MAC address prefix (default: random)')
    parser.add_argument('--revert', action='store_true', help='Revert to original MAC address')

    args = parser.parse_args()

    spoofer = MacSpoofer(args.interface, args.manufacturer)

    interfaces = [args.interface] if args.interface else spoofer.get_interfaces()

    for interface in interfaces:
        if args.revert:
            spoofer.revert_mac(interface)
        else:
            new_mac = spoofer.generate_mac()
            spoofer.change_mac(new_mac, interface)


if __name__ == "__main__":
    main()
