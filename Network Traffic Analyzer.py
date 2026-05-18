from scapy.all import sniff

def analyze_packet(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        protocol = packet["IP"].proto
        
        protocol_name = "Unknown"
        if protocol == 6:
            protocol_name = "TCP"
        elif protocol == 17:
            protocol_name = "UDP"
        
        print(f"Source: {src_ip} | Destination: {dst_ip} | Protocol: {protocol_name}")

print("Starting Network Traffic Analyzer...")
print("Press Ctrl+C to stop\n")

sniff(prn=analyze_packet, count=20)