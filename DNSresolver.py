import socket

# get domain name from user
domain = input("Enter domain name (example.com): ")

try:
    # convert domain name to IP address using DNS
    ip = socket.gethostbyname(domain)
    
    # print the results
    print(f"Domain: {domain}")
    print(f"IP Address: {ip}")
    
except socket.gaierror:
    # if domain doesn't exist or DNS lookup fails, catch the error
    print(f"Could not resolve {domain}")