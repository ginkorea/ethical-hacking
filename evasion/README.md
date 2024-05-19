# Spoofer

This Python script allows you to spoof your MAC address for penetration testing purposes. It provides functionalities to change the MAC address, revert it to the original, scan the local subnet for available MAC addresses, and perform ARP spoofing.

## Requirements

- Python 3
- `arp-scan` and `arpspoof` tools installed

To install the required tools on Fedora:
```sh
sudo dnf install arp-scan dsniff
```

## Usage

### Arguments

- `-i`, `--interface`: Network interface to spoof (default: all)
- `-m`, `--manufacturer`: Manufacturer for MAC address prefix (default: random)
- `--revert`: Revert to the original MAC address
- `--scan`: Scan subnet for available MAC addresses
- `--overwrite-cam`: Overwrite CAM of the local router
- `--arp-spoof`: ARP spoof devices to believe you are the gateway
- `--router-ip`: IP address of the router for CAM overwriting
- `--target-ip`: IP address of the target device for ARP spoofing

### Examples

#### Change MAC Address
Change the MAC address of a specific interface to a random address from a specified manufacturer.
```sh
sudo python spoofer.py -i wlo1 -m samsung
```

#### Revert to Original MAC Address
Revert the MAC address of a specific interface to the original.
```sh
sudo python spoofer.py -i wlo1 --revert
```

#### Scan Subnet
Scan the subnet for available MAC addresses.
```sh
sudo python spoofer.py --scan
```

#### Overwrite CAM
Overwrite the CAM of the local router with a specified target MAC address.
```sh
sudo python spoofer.py --overwrite-cam --router-ip 192.168.1.1
```

#### ARP Spoofing
ARP spoof devices to believe you are the gateway.
```sh
sudo python spoofer.py --arp-spoof --router-ip 192.168.1.1 --target-ip 192.168.1.100
```

## Script

Please refer to the `spoofer.py` file in the repository for the full script implementation.