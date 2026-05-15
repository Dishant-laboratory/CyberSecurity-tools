import requests

url = input("Enter website URL (https://example.com): ")

try:
    response = requests.get(url)
    
    print(f"URL: {url}\n")
    print("Response Headers:")
    
    for header, value in response.headers.items():
        print(f"{header}: {value}")
    
    print(f"\nStatus Code: {response.status_code}")
    
except Exception as e:
    print(f"Error: {e}")