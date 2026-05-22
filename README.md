# 🔍 Python Packet Sniffer

A lightweight network packet sniffer built with [Scapy](https://scapy.net/) for educational and authorized network monitoring.

---

## ⚠️ Legal & Ethical Notice

> **This tool is for EDUCATIONAL and AUTHORIZED use only.**
> Unauthorized packet sniffing on networks you do not own or have explicit permission to monitor is **illegal** and may violate laws such as the Computer Fraud and Abuse Act (CFAA) and similar legislation in other jurisdictions.
> **Always obtain proper authorization before running this tool.**

---

## Features

- Captures live TCP, UDP, and ICMP packets in real time
- Displays source/destination IP addresses and port numbers
- Shows raw payload data when present
- Timestamps every captured packet
- Graceful exit with a summary on `Ctrl+C`

---

## Requirements

- Python 3.6+
- [Scapy](https://scapy.net/)

Install Scapy via pip:

```bash
pip install scapy
```

> **Note:** On Linux/macOS, packet sniffing requires root/administrator privileges. Run the script with `sudo`.

---

## Usage

```bash
# Linux / macOS
sudo python packet_sniffer.py

# Windows (run as Administrator)
python packet_sniffer.py
```

Press `Ctrl+C` to stop sniffing. A summary will be printed showing total packets captured and the stop time.

---

## Sample Output

```
============================================================
⚠️  ETHICAL NOTICE:
    This tool is for EDUCATIONAL and AUTHORIZED use only.
    Do NOT use this tool on networks you don't own or
    have explicit permission to monitor.
    Unauthorized packet sniffing is ILLEGAL.
============================================================

🔍 Sniffing packets... Press Ctrl+C to stop.

[Packet #1] | Timestamp: 2024-01-15 10:23:45
------------------------------------------------------------
  Protocol        : TCP
  Source IP       : 192.168.1.10:54321
  Destination IP  : 93.184.216.34:443
  Payload         : No payload data
------------------------------------------------------------

[Packet #2] | Timestamp: 2024-01-15 10:23:46
------------------------------------------------------------
  Protocol        : UDP
  Source IP       : 192.168.1.10:12345
  Destination IP  : 8.8.8.8:53
  Payload         : b'\x00\x01...'
------------------------------------------------------------

============================================================
  ✅ Sniffing stopped by user.
  📦 Total Packets Captured: 2
  🕒 Stopped at: 2024-01-15 10:23:50
============================================================
```

---

## Supported Protocols

| Protocol | Details Captured |
|----------|-----------------|
| TCP | Source/destination IP & port, payload |
| UDP | Source/destination IP & port, payload |
| ICMP | Source/destination IP only |

---

## Project Structure

```
packet_sniffer.py   # Main script
README.md           # Documentation
```

---

## Limitations

- Only processes packets with an IP layer; non-IP traffic (e.g., ARP) is ignored.
- Payload is displayed as raw bytes; no application-layer decoding (HTTP, DNS, etc.).
- No logging to file — output is console only.

---

## Potential Improvements

- Filter packets by IP, port, or protocol via command-line arguments
- Save captured packets to a `.pcap` file for analysis in Wireshark
- Add application-layer parsing (e.g., HTTP headers, DNS queries)
- Build a live statistics dashboard

---

## License

This project is intended for educational use. Please use responsibly and in accordance with all applicable laws.
