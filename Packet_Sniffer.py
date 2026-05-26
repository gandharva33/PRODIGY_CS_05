from scapy.all import sniff, TCP, UDP, ICMP, IP, Raw
from datetime import datetime

# ============================================================
# ⚠️  ETHICAL NOTICE
# ============================================================
print("=" * 60)
print("⚠️  ETHICAL NOTICE:")
print("    This tool is for EDUCATIONAL and AUTHORIZED use only.")
print("    Do NOT use this tool on networks you don't own or")
print("    have explicit permission to monitor.")
print("    Unauthorized packet sniffing is ILLEGAL.")
print("=" * 60)
print()

# ============================================================
# Counters
# ============================================================
packet_count = 0
protocol_counts = {"TCP": 0, "UDP": 0, "ICMP": 0, "Other": 0}

# ============================================================
# Packet Handler
# ============================================================
def process_packet(packet):
    global packet_count
    packet_count += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n[Packet #{packet_count}] | Timestamp: {timestamp}")
    print("-" * 60)

    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if packet.haslayer(TCP):
            protocol_counts["TCP"] += 1
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

            print(f"  Protocol        : TCP")
            print(f"  Source IP       : {src_ip}:{src_port}")
            print(f"  Destination IP  : {dst_ip}:{dst_port}")

            if packet.haslayer(Raw):
                payload = packet[Raw].load
                print(f"  Payload         :\n{payload}")
            else:
                print(f"  Payload         : No payload data")

        elif packet.haslayer(UDP):
            protocol_counts["UDP"] += 1
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

            print(f"  Protocol        : UDP")
            print(f"  Source IP       : {src_ip}:{src_port}")
            print(f"  Destination IP  : {dst_ip}:{dst_port}")

            if packet.haslayer(Raw):
                payload = packet[Raw].load
                print(f"  Payload         :\n{payload}")
            else:
                print(f"  Payload         : No payload data")

        elif packet.haslayer(ICMP):
            protocol_counts["ICMP"] += 1

            print(f"  Protocol        : ICMP")
            print(f"  Source IP       : {src_ip}")
            print(f"  Destination IP  : {dst_ip}")

        else:
            protocol_counts["Other"] += 1

            print(f"  Protocol        : Other/Unknown")
            print(f"  Source IP       : {src_ip}")
            print(f"  Destination IP  : {dst_ip}")

    else:
        # ✅ Catches ARP, IPv6 and other non-IP packets
        protocol_counts["Other"] += 1
        pkt_type = packet.name if hasattr(packet, "name") else "Unknown"

        print(f"  Protocol        : Non-IP ({pkt_type})")
        print(f"  Info            : {packet.summary()}")

    print("-" * 60)

# ============================================================
# Start Sniffing
# ============================================================
try:
    print("🔍 Sniffing packets... Press Ctrl+C to stop.\n")
    sniff(prn=process_packet, store=0)

except KeyboardInterrupt:
    print("\n" + "=" * 60)
    print(f"  ✅ Sniffing stopped by user.")
    print(f"  🕒 Stopped at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # ✅ Protocol breakdown with visual bar chart
    print(f"\n  📦 PACKET SUMMARY")
    print(f"  {'─' * 40}")
    print(f"  {'Total Packets':<16}: {packet_count}")
    print(f"  {'─' * 40}")

    for proto, count in protocol_counts.items():
        bar = "█" * count
        pct = (count / packet_count * 100) if packet_count > 0 else 0
        print(f"  {proto:<6}: {count:<5} {bar:<30} {pct:.1f}%")

    print("=" * 60)
