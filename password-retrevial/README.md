# Linux-Based Password Retrieval Tools

This document provides a list of Linux-based password retrieval tools and their installation instructions for Fedora Linux.

## 1. LaZagne

LaZagne is an open-source project used to retrieve passwords stored on a local computer.

### Installation

```bash
# Install dependencies
sudo dnf install python3-pip

# Clone the repository
git clone https://github.com/AlessandroZ/LaZagne.git

# Navigate to the directory
cd LaZagne

# Install required Python packages
pip3 install -r requirements.txt

# Run LaZagne
python3 laZagne.py
```

## 2. mimipenguin

mimipenguin is a simple, standalone tool that extracts plaintext credentials from memory on Linux systems.

### Installation

```bash
# Install dependencies
sudo dnf install git gcc

# Clone the repository
git clone https://github.com/huntergregal/mimipenguin.git

# Navigate to the directory
cd mimipenguin

# Compile the tool
gcc mimipenguin.c -o mimipenguin

# Run mimipenguin
sudo ./mimipenguin
```

## 3. creddump7

creddump7 is a collection of Python scripts to extract credentials from various sources on Windows, also usable on Linux systems for forensic analysis.

### Installation

```bash
# Install dependencies
sudo dnf install python3-pip

# Clone the repository
git clone https://github.com/Neohapsis/creddump7.git

# Navigate to the directory
cd creddump7

# Run one of the scripts (example: cachedump)
python3 cachedump.py
```

## 4. Hashcat

Hashcat is a powerful password recovery tool. It is designed to break even the most complex passwords.

### Installation

```bash
# Install hashcat
sudo dnf install hashcat

# Example usage: Crack a hash
hashcat -m 0 -a 0 hash.txt wordlist.txt
```

## 5. John the Ripper

John the Ripper is a fast password cracker, currently available for many flavors of Unix.

### Installation

```bash
# Install John the Ripper
sudo dnf install john

# Example usage: Crack a password hash
john --wordlist=wordlist.txt hash.txt
```

## 6. THC-Hydra

THC-Hydra is a fast and flexible password cracking tool, supporting many protocols.

### Installation

```bash
# Install THC-Hydra
sudo dnf install hydra

# Example usage: Brute-force attack on FTP
hydra -l username -P passwordlist.txt ftp://target
```

## 7. ophcrack

ophcrack is a Windows password cracker based on Rainbow Tables.

### Installation

```bash
# Install ophcrack
sudo dnf install ophcrack

# Run ophcrack
ophcrack
```

## 8. RSMangler

RSMangler is a wordlist generator that mangles your wordlist based on several rules.

### Installation

```bash
# Install RSMangler
sudo dnf install git

# Clone the repository
git clone https://github.com/ryhanson/wordlistgen.git

# Navigate to the directory
cd wordlistgen

# Run RSMangler
./rsmangler.pl -f wordlist.txt
```

## 9. PwDump7

PwDump7 is a Windows password hash dumper.

### Installation

```bash
# Download PwDump7 binary
wget http://www.tarasco.org/security/pwdump_7/pwdump7

# Make it executable
chmod +x pwdump7

# Run PwDump7 (requires administrative privileges)
sudo ./pwdump7
```

This document provides a variety of tools for password retrieval on Linux systems. Use these tools responsibly and only for authorized testing and educational purposes.
