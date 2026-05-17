import hashlib
import os

def calculate_hash(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

file_path = input("Enter file path to monitor: ")

if os.path.exists(file_path):
    original_hash = calculate_hash(file_path)
    print(f"Original hash: {original_hash}")
    print("File is being monitored. If file changes hash will be different.")
    
    input("Press Enter after modifying the file to check...")
    
    new_hash = calculate_hash(file_path)
    print(f"New hash: {new_hash}")
    
    if original_hash == new_hash:
        print("File has NOT been modified")
    else:
        print("WARNING: File HAS been modified")
else:
    print("File not found")