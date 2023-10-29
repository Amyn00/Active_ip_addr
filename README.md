# Active IP Adresse
## Discovering Active IP Addresses
This Python script uses Scapy to discover active IP addresses on a local network using ARP and resolves device names using the Domain Name System (DNS).
## Usage
1. Ensure you have Python 3 installed on your system.
```bash
python3 --version
```
2. Install the required Python libraries by running the following command:
```bash
pip install scapy tabulate
```
## How to Start
1. Clone the repository to your local machine:
```bach
git clone https://github/Amyn00/Active_ip_addr.git
```
2. Navigate to the project directory:
```bash
cd Active_ip_addr
```
3. Run the following commande, replacing 192.168.1.1/24 with the range of IP addresses you want to analyze:
```bash
python3 showip.py 192.168.1.1/24
```
or
```bash
./showip.py 192.168.1.1/24
```
The script will discover active IP addresses, resolve device names via DNS, and display the information in a table.

## Configuration
Ensure that your network allows DNS name resolution. Device names depend on your network configuration and the availability of DNS servers capable of resolving these names.
## Example Output
```bash
+----------------+-------------------+------------------+
|   IP Address   |   MAC Address     |    Device Name   |
+================+===================+==================+
| 192.168.1.1    | 00:1A:2B:3C:4D:5E | MyRouter         |
| 192.168.1.2    | 00:1A:2B:3C:4D:5F | N/A              |
| 192.168.1.3    | 00:1A:2B:3C:4D:60 | N/A              |
| ...            | ...               | ...              |
+----------------+-------------------+------------------+

```
This script is provided as an example and may require adjustments based on your specific network. Name resolution depends on your network's DNS configuration.

## Author
**Mohammed Amine Mounjid**
