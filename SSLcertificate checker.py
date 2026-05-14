import ssl
import socket

domain = input("Enter domain name (example.com): ")

try:
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=domain)
    conn.connect((domain, 443))
    
    cert = conn.getpeercert()
    
    print(f"Domain: {domain}")
    print(f"Issuer: {cert['issuer']}")
    print(f"Subject: {cert['subject']}")
    print(f"Expires: {cert['notAfter']}")
    
    conn.close()
    
except Exception as e:
    print(f"Error: {e}")