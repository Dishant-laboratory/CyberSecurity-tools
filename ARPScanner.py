import subprocess
import re

# get your network range
network = input("Enter network range (example: 192.168.1.0/24): ")

print(f"Scanning {network} for active devices...\n")

# use nmap to scan network
result = subprocess.run(['nmap', '-sn', network], capture_output=True, text=True)

# parse output to find IP addresses
ips = re.findall(r'(\d+\.\d+\.\d+\.\d+)', result.stdout)

print(f"Found {len(ips)} devices on network:")
for ip in ips:
    print(f"  {ip}")