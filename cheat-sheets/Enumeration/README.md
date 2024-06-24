### CEH Exam Prep Module 4: Enumeration Cheat Sheet

#### 1. NetBIOS Enumeration using Windows Command-Line Utilities

**Objective**: Gather information about network shares, user accounts, and more using NetBIOS.

**Commands**:
1. **nbtstat**: This command displays NetBIOS over TCP/IP protocol statistics.
   - `nbtstat -n`: Lists local NetBIOS names.
   - `nbtstat -A <IP address>`: Lists remote machine's NetBIOS names table.
   - `nbtstat -c`: Displays the NetBIOS name cache.

**Example**:
```sh
nbtstat -A 192.168.1.10
```

**Explanation**: The above command queries the NetBIOS names and MAC addresses for the host with the IP address `192.168.1.10`.

#### 2. SNMP Enumeration using SnmpWalk

**Objective**: Enumerate SNMP-enabled devices to extract useful information like network configuration and device details.

**Commands**:
1. **snmpwalk**: This command retrieves a subtree of management values using SNMP GETNEXT requests.
   - `snmpwalk -v 2c -c <community string> <IP address>`

**Example**:
```sh
snmpwalk -v 2c -c public 192.168.1.1
```

**Explanation**: The above command uses SNMP version 2c with the community string "public" to walk through the SNMP tree on the device at `192.168.1.1`.

#### 3. LDAP Enumeration using Active Directory Explorer (AD Explorer)

**Objective**: Extract information from LDAP directories, particularly Active Directory, to gather details about users, groups, and other objects.

**Steps**:
1. **Download and Install AD Explorer**: Obtain the tool from the Microsoft website.
2. **Connect to Active Directory**:
   - Open AD Explorer.
   - Click on "File" -> "Connect".
   - Enter the domain controller’s name and appropriate credentials.

3. **Browse and Export Data**:
   - Navigate through the directory tree to enumerate objects.
   - Use the export feature to save data for analysis.

**Example**:
Navigate to "CN=Users,DC=example,DC=com" to view all user accounts in the domain.

**Explanation**: AD Explorer allows you to navigate and search through Active Directory objects, making it easier to enumerate user accounts, groups, and other directory information.

#### 4. NFS Enumeration using RPCScan and SuperEnum

**Objective**: Identify and enumerate shared directories and files on NFS (Network File System).

**Commands**:
1. **rpcinfo**: Displays RPC services running on a target system.
   - `rpcinfo -p <target IP>`

2. **showmount**: Lists NFS exports on a remote host.
   - `showmount -e <target IP>`

**Example**:
```sh
rpcinfo -p 192.168.1.20
showmount -e 192.168.1.20
```

**Explanation**: `rpcinfo -p` lists RPC services available on the target, while `showmount -e` lists all exported file systems from the NFS server at `192.168.1.20`.

#### 5. DNS Enumeration using Zone Transfer

**Objective**: Perform a DNS zone transfer to gather detailed DNS records from a domain.

**Commands**:
1. **nslookup**: Interactive DNS query tool.
   - `nslookup`
     - `server <DNS server IP>`
     - `set type=any`
     - `<target domain>`
     - `ls -d <target domain>`

**Example**:
```sh
nslookup
server 8.8.8.8
set type=any
example.com
ls -d example.com
```

**Explanation**: This sequence of commands changes the DNS server to `8.8.8.8`, sets the query type to `any`, and attempts a zone transfer for `example.com`.

#### 6. SMTP Enumeration using Nmap

**Objective**: Enumerate SMTP servers to identify valid email accounts and other server details.

**Commands**:
1. **Nmap with NSE scripts**:
   - `nmap -p 25 --script smtp-enum-users <target IP>`

**Example**:
```sh
nmap -p 25 --script smtp-enum-users 192.168.1.30
```

**Explanation**: The above Nmap command runs an SMTP user enumeration script against the target IP `192.168.1.30` on port `25`.

#### 7. Enumeration using Various Tools (Global Network Inventory)

**Objective**: Use Global Network Inventory to gather comprehensive information about network devices.

**Steps**:
1. **Download and Install Global Network Inventory**: Obtain the tool from the vendor’s website.
2. **Configure a Scan**:
   - Open Global Network Inventory.
   - Configure a new scan by specifying the IP range or domain.
   - Set appropriate credentials for accessing network devices.

3. **Run the Scan**:
   - Execute the scan to gather information on network devices, including OS details, installed software, hardware information, etc.

**Example**:
Configure a scan for the IP range `192.168.1.1 - 192.168.1.254` with admin credentials.

**Explanation**: Global Network Inventory will scan the specified IP range and return detailed information about each device, which can be used for further enumeration and analysis.

---

This cheat sheet covers the essential commands and steps for performing various enumeration tasks in Module 4 of the CEH exam prep. Each section provides the necessary commands, examples, and explanations to help you understand and execute these tasks effectively.