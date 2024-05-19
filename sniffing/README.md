# Linux-Based Sniffing Tools

This document provides a list of Linux-based sniffing tools and their installation instructions for Fedora Linux.

## 1. Wireshark

Wireshark is a widely-used network protocol analyzer.

### Installation

```bash
# Install Wireshark
sudo dnf install wireshark

# Run Wireshark (with root privileges)
sudo wireshark
```

## 2. tcpdump

tcpdump is a powerful command-line packet analyzer.

### Installation

```bash
# Install tcpdump
sudo dnf install tcpdump

# Example usage: Capture packets on interface eth0
sudo tcpdump -i eth0
```

## 3. Ettercap

Ettercap is a comprehensive suite for man-in-the-middle attacks on LAN.

### Installation

```bash
# Install Ettercap
sudo dnf install ettercap

# Run Ettercap in text mode
sudo ettercap -T -i eth0
```

## 4. Kismet

Kismet is a wireless network detector, sniffer, and intrusion detection system.

### Installation

```bash
# Install Kismet
sudo dnf install kismet

# Run Kismet
sudo kismet
```

## 5. Tshark

Tshark is the command-line version of Wireshark.

### Installation

```bash
# Install Tshark
sudo dnf install wireshark-cli

# Example usage: Capture packets on interface eth0
sudo tshark -i eth0
```

## 6. Nmap

Nmap is a network scanning tool that can also be used for sniffing.

### Installation

```bash
# Install Nmap
sudo dnf install nmap

# Example usage: Scan a network
sudo nmap -sn 192.168.1.0/24
```

## 7. dsniff

dsniff is a collection of tools for network auditing and penetration testing.

### Installation

```bash
# Install dsniff
sudo dnf install dsniff

# Example usage: Sniff passwords
sudo dsniff -i eth0
```

## 8. Driftnet

Driftnet watches network traffic and picks out images from TCP streams.

### Installation

```bash
# Install Driftnet
sudo dnf install driftnet

# Example usage: Capture images on interface eth0
sudo driftnet -i eth0
```

## 9. URLsnarf

URLsnarf outputs all URLs sniffed from HTTP traffic.

### Installation

```bash
# Install URLsnarf
sudo dnf install dsniff

# Example usage: Capture URLs on interface eth0
sudo urlsnarf -i eth0
```

## 10. Snort

Snort is an open-source network intrusion prevention system and network intrusion detection system.

### Installation

```bash
# Install Snort
sudo dnf install snort

# Example usage: Run Snort in network sniffer mode
sudo snort -v -i eth0
```

## 11. Aircrack-ng

Aircrack-ng is a suite of tools to assess WiFi network security.

### Installation

```bash
# Install Aircrack-ng
sudo dnf install aircrack-ng

# Example usage: Capture packets on interface wlan0
sudo airodump-ng wlan0
```

This document provides a variety of tools for sniffing network traffic on Linux systems. Use these tools responsibly and only for authorized testing and educational purposes.