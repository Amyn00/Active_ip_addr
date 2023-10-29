#!/usr/bin/env python3

import scapy.all as scapy
from tabulate import tabulate
import socket
import sys

def get_device_name(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "N/A"

def scan(ip):
    # Create an ARP object to query the ARP table
    arp_request = scapy.ARP(pdst=ip)

    # Create an Ethernet packet containing the ARP request
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # Combine the Ethernet packet and the ARP request
    arp_request_packet = ether/arp_request

    # Send the ARP packet and receive responses
    answered_list = scapy.srp(arp_request_packet, timeout=5, verbose=False)[0]

    # List to store discovered IP addresses, device names, and MAC addresses
    devices = []

    # Iterate through the responses to extract IP addresses, device names, and MAC addresses
    for element in answered_list:
        device_info = [element[1].psrc, element[1].hwsrc, get_device_name(element[1].psrc)]
        devices.append(device_info)

    return devices


if len(sys.argv) != 2:
    print("Usage: python3 showip.py <IP_RANGE>\n    EX: python3 showip.py 192.168.1.1/24")
    sys.exit(1)

ip_range = sys.argv[1]

# Call the scan function with the specified IP address range
active_devices = scan(ip_range)

# Display active IP addresses, device names, and MAC addresses in a table
headers = ["Adresse IP", "Adresse MAC", "Peripheric Name"]
table = tabulate(active_devices, headers, tablefmt="grid")
print(table)

