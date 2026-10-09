# 🧪 Project #1 — Network Traffic Analyzer

> **Phase 2 Capstone: Networking — On The Wire**  
> *"Build your own miniature Wireshark in Python to analyze live traffic and PCAP captures."*

---

## 🎯 Project Goals

As outlined in the master roadmap (`readme.md`), this tool captures packets from your lab and extracts:

1. **Source & Destination IPs** (Who is talking to whom?)
2. **Protocol Breakdown** (TCP vs. UDP vs. ICMP vs. ARP)
3. **Port Numbers & Top Talkers** (Which ports are most active?)
4. **Packet Counts & Bandwidth Volume**
5. **DNS Queries Sniffing** (What domain names are machines looking up?)
6. **HTTP Requests Extraction** (What unencrypted web pages are being requested?)
7. **Terminal Dashboard Summary** (Formatted tables and statistics)

---

## 🏗️ Architecture & Modules

```text
09-project-traffic-analyzer/
├── analyzer.py       # Core packet sniffer & parser engine
├── visualizer.py     # Clean terminal dashboard & summary tables
├── sample.pcap       # Test packet capture file
└── README.md         # Guide & usage instructions
```

---

## 🚀 Implementation Complete

- [x] **Step 1:** Environment setup (`python3-scapy`).
- [x] **Step 2:** Minimal live sniffer test (`test_sniff.py`).
- [x] **Step 3:** Layer 3 & Layer 4 extraction (IPs, Ports, Protocols).
- [x] **Step 4:** Layer 7 deep packet inspection (DNS queries & HTTP methods).
- [x] **Step 5:** Aggregation metrics & rich terminal dashboard.
- [x] **Step 6:** Live traffic testing in your WSL lab.

