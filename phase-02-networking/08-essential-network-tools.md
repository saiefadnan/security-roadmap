# 🛠️ Step 8: Essential Network Tools (The Operator's Toolkit)

> **Phase 2: Networking — On The Wire**  
> *"Tools do not make a hacker; understanding the bytes they send and receive does."*

---

## 1. Overview of the Operator's Toolkit

| Tool | Primary Purpose | Layer | Common Use Case |
| :--- | :--- | :--- | :--- |
| **`nc` (Netcat)** | Raw TCP/UDP read & write | Layer 4 | Banner grabbing, ad-hoc listeners, reverse shells. |
| **`traceroute`** | Path & hop enumeration | Layer 3 | Mapping routers between source and destination using IP TTL. |
| **`nmap`** | Port scanning & fingerprinting | Layer 4 & 7 | Host discovery, service version detection, OS identification, vulnerability scanning. |
| **`tcpdump` / Wireshark** | Packet capture & deep packet inspection | Layers 2–7 | Sniffing wire traffic, analyzing handshakes, extracting raw protocols. |

---

## 2. Netcat (`nc`) — The "Swiss Army Knife"

### A. Banner Grabbing (Client Mode)
Connecting to a service to see what software version it discloses:
```bash
# Connect to HTTP on port 80:
nc -v scanme.nmap.org 80
# Send a basic HTTP request:
HEAD / HTTP/1.0
```
- **Recon output:** Discloses web server, version, and OS (e.g. `Server: Apache/2.4.7 (Ubuntu)`).

### B. Creating a Listener (Server Mode)
```bash
nc -lvnp 4444
```
- `-l`: Listen mode
- `-v`: Verbose
- `-n`: Numeric (no reverse DNS lookup)
- `-p 4444`: Port number

---

## 3. `traceroute` — The TTL Trick

### How it works:
- Every IP packet has an 8-bit **TTL (Time to Live)** field.
- Each intermediate router decrements `TTL` by 1.
- When `TTL == 0`, the router drops the packet and sends back `ICMP Type 11 (Time Exceeded in Transit)`.
- `traceroute` systematically increments TTL (`TTL=1, 2, 3...`), forcing each consecutive router along the path to identify itself.

### Command:
```bash
traceroute -n -m 15 -q 1 1.1.1.1
```
- Maps the path from local virtual adapter $\rightarrow$ home router $\rightarrow$ ISP CGNAT $\rightarrow$ Internet Exchange Point (IXP) $\rightarrow$ Cloudflare edge node.

---

## 4. Nmap (Network Mapper)

### The 3 Core Port States:
- **`open`:** Target answered with `SYN-ACK`. A service is actively listening.
- **`closed`:** Target answered with `RST`. Host is up, but no service is bound to that port.
- **`filtered`:** Firewall silently dropped the packet (`DROP`). Nmap received no reply.

### Core Scanning Commands:
```bash
# 1. Fast service version scan on specific ports:
nmap -sV -p 22,80 scanme.nmap.org

# 2. Host discovery (Ping Sweep across a subnet):
nmap -sn 192.168.1.0/24

# 3. Stealth SYN Scan (Requires root; sends RST before completing handshake):
sudo nmap -sS -p 1-1000 scanme.nmap.org

# 4. Comprehensive scan (Versions, OS detection, Default scripts):
nmap -sC -sV -O scanme.nmap.org
```

---

## 5. `tcpdump` & Wireshark

### Live Packet Sniffing on an Interface:
```bash
# Capture first 10 packets on interface eth0:
sudo tcpdump -i eth0 -n -c 10

# Filter only HTTP traffic (port 80):
sudo tcpdump -i eth0 -n "tcp port 80"

# Save capture to a .pcap file for analysis in Wireshark:
sudo tcpdump -i eth0 -w capture.pcap
```
