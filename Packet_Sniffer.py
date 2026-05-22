from scapy.all import sniff, TCP, UDP, ICMP, IP, Raw
from datetime import datetime

# ⚠️ Ethical Notice
print("=" * 60)
print("⚠️  ETHICAL NOTICE:")
print("    This tool is for EDUCATIONAL and AUTHORIZED use only.")
print("    Do NOT use this tool on networks you don't own or")
print("    have explicit permission to monitor.")
print("    Unauthorized packet sniffing is ILLEGAL.")
print("=" * 60)
print()

# Packet counter
packet_count = 0

# Function to process each packet
def process_packet(packet):
    global packet_count
    packet_count += 1

    # Timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if packet.haslayer(IP):  # Check if the packet has an IP layer
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        print(f"\n[Packet #{packet_count}] | Timestamp: {timestamp}")
        print("-" * 60)

        # Analyze by protocol
        if packet.haslayer(TCP):
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

            print(f"  Protocol        : {protocol}")
            print(f"  Source IP       : {src_ip}:{src_port}")
            print(f"  Destination IP  : {dst_ip}:{dst_port}")

            if packet.haslayer(Raw):  # If there's payload data
                payload = packet[Raw].load
                print(f"  Payload         :\n{payload}")
            else:
                print(f"  Payload         : No payload data")

        elif packet.haslayer(UDP):
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

            print(f"  Protocol        : {protocol}")
            print(f"  Source IP       : {src_ip}:{src_port}")
            print(f"  Destination IP  : {dst_ip}:{dst_port}")

            if packet.haslayer(Raw):  # If there's payload data
                payload = packet[Raw].load
                print(f"  Payload         :\n{payload}")
            else:
                print(f"  Payload         : No payload data")

        elif packet.haslayer(ICMP):
            protocol = "ICMP"

            print(f"  Protocol        : {protocol}")
            print(f"  Source IP       : {src_ip}")
            print(f"  Destination IP  : {dst_ip}")

        print("-" * 60)

# Graceful exit on Ctrl+C
try:
    print("🔍 Sniffing packets... Press Ctrl+C to stop.\n")
    sniff(prn=process_packet, store=0)

except KeyboardInterrupt:
    print("\n" + "=" * 60)
    print(f"  ✅ Sniffing stopped by user.")
    print(f"  📦 Total Packets Captured: {packet_count}")
    print(f"  🕒 Stopped at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
