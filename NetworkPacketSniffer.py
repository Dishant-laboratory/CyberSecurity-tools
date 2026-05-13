from scapy.all import sniff

def packet_callback(packet):
    print(f"Packet captured: {packet.summary()}")

print("Starting packet sniffer...")
print("Press Ctrl+C to stop\n")

sniff(prn=packet_callback, count=10)