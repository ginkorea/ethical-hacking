# MAC Address Spoofer

## Description

`mac_spoofer.py` is a Python script designed to spoof the MAC address of network interfaces. This can be useful for various purposes, such as privacy protection, network security testing, and bypassing MAC address filtering.

## Requirements

- Python 3
- `subprocess` module (included in the Python standard library)
- Root privileges to execute network interface changes

## Usage

### Basic Usage

To run the script with default settings, which will spoof the MAC address of all network interfaces with a randomly chosen manufacturer prefix:

```sh
sudo python3 mac_spoof.py
```

### Specify Network Interface and Manufacturer

You can specify a particular network interface and a manufacturer prefix:

```sh
sudo python3 mac_spoof.py -i <interface> -m <manufacturer>
```

- `<interface>`: The network interface to spoof (e.g., `eth0`, `wlan0`).
- `<manufacturer>`: The manufacturer for the MAC address prefix. Options are `samsung`, `sony`, `dell`, and `konko`.

Example:

```sh
sudo python3 mac_spoof.py -i eth0 -m samsung
```

### Revert to Original MAC Address

To revert a specific network interface to its original MAC address:

```sh
sudo python3 mac_spoof.py -i <interface> --revert
```

Example:

```sh
sudo python3 mac_spoof.py -i eth0 --revert
```

### Help

To display the help message and see all options:

```sh
python3 mac_spoof.py -h
```

## Script Details

### Class: `MacSpoofer`

This class handles MAC address spoofing.

#### Methods

- `__init__(self, interface=None, manufacturer=None)`: Initializes the MacSpoofer with an interface and manufacturer.
- `get_interfaces(self)`: Returns a list of all network interfaces.
- `generate_mac(self)`: Generates a new MAC address based on the chosen manufacturer.
- `change_mac(self, new_mac, interface)`: Changes the MAC address of the specified interface to the new MAC address.
- `revert_mac(self, interface)`: Reverts the MAC address of the specified interface to its original MAC address.
- `get_original_mac(self, interface)`: Gets the original MAC address of the specified interface.

## Example Manufacturers

- samsung
- sony
- dell
- konko

## Notes

- Ensure you have Python installed on your system.
- Changing MAC addresses is useful for certain pentesting activities but should be done responsibly and within legal boundaries.

## License

This project is licensed under the GNU General Public License V3.

