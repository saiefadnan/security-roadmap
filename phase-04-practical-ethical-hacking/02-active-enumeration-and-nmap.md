# 🔍 Step 2: Active Enumeration & Nmap Mastery

> **Phase 4: Practical Ethical Hacking**  
> *"If passive recon is reading the blueprint of a building from public archives, active enumeration is walking up to the building, testing every door handle, and looking through every window."*

---

## 1. What is Active Enumeration?

In **Active Enumeration**, we make **direct network contact** with the target machine. We send probe packets to uncover:
1. **Which IP addresses are actually online?** (Host Discovery)
2. **Which doors (ports) are open?** (Port Scanning)
3. **What specific software and versions are running behind those doors?** (Service Fingerprinting)
4. **What operating system is running?** (OS Detection)
5. **Are there obvious security misconfigurations or known bugs?** (Script Scanning)

---

## 2. How Port Scanning Works (TCP Handshake Mechanics)

Remember the **TCP 3-Way Handshake** (`SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`) from Phase 2? Nmap manipulates this handshake to detect open ports:

### A. TCP Connect Scan (`-sT`) — The "Full" Handshake
* **How it works:** Your computer completes the entire 3-way handshake with the target port (`SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`), then gracefully disconnects with `RST` or `FIN`.
* **Pros:** Highly reliable; does not require root privileges.
* **Cons:** Slower; easily logged in the target's application access logs.

### B. TCP SYN Scan (`-sS`) — The "Stealth / Half-Open" Scan (Default for Root)
* **How it works:**
  ```text
  Attacker                           Target Port
     │                                    │
     │ ──── 1. SYN (Knock on door) ─────> │
     │ <─── 2. SYN-ACK (Door is open!) ── │
     │ ──── 3. RST (Reset! Never mind!) ─> │  <-- Closes connection immediately!
  ```
* **Pros:** Extremely fast; the connection is aborted before the target application creates a full session log entry.
* **Cons:** Requires `sudo` / root privileges on Linux.

### C. UDP Scan (`-sU`)
* UDP has no handshake or acknowledgment packets.
* Nmap sends empty UDP packets. If it receives an **ICMP Port Unreachable** error, the port is `closed`. If no response comes back, it is `open|filtered`.
* Useful for finding DNS (Port 53), SNMP (Port 161), and DHCP (Port 67).

---

## 3. The 3 Port States in Nmap

When Nmap finishes scanning a port, it labels it with one of three primary states:

| State | What It Means | Network Cause |
| :--- | :--- | :--- |
| **`open`** | A program is actively listening and accepted our connection. | The server replied with `SYN-ACK`. |
| **`closed`** | The machine is online, but no service is listening on this port. | The server replied with `RST` (Reset). |
| **`filtered`** | A firewall or router is blocking access; Nmap cannot tell if it's open. | Packets were dropped silently or blocked by a firewall. |

---

## 4. The 4 Stages of a Professional Nmap Scan

Real penetration testers don't scan all 65,535 ports at once with heavy scripts—that takes hours and triggers firewalls. They scan in **4 progressive stages**:

### Stage 1: Host Discovery (Ping Sweep)
Find which computers on a subnet are alive without scanning any ports:
```bash
nmap -sn 192.168.1.0/24
```
*(The `-sn` flag disables port scanning and only checks if hosts respond to ICMP/ARP).*

---

### Stage 2: Quick Top-Port Reconnaissance
Scan the top 1,000 most common ports fast:
```bash
nmap -T4 10.10.10.5
```
*(The `-T4` flag speeds up scan timing).*

---

### Stage 3: Full Port Sweep (All 65,535 Ports)
Attackers and administrators often hide sensitive services (like admin panels or SSH) on strange high-number ports like `8080`, `2222`, or `49152`:
```bash
nmap -p- -T4 10.10.10.5
```
*(The `-p-` flag scans ports 1 through 65,535).*

---

### Stage 4: The Deep Dive (Services, Versions & Vulnerability Scripts)
Once you know exactly which ports are open (e.g. `22, 80, 443`), run the comprehensive detection suite only on those specific ports:
```bash
nmap -p 22,80,443 -sV -sC -O -T4 10.10.10.5
```

Where:
* **`-sV`**: **Service Version Detection** — Grabs banners and probes services to find exact software versions (e.g., `Apache 2.4.52`, `OpenSSH 8.9p1`).
* **`-sC`**: **Default Scripts** — Runs safe, automated Lua scripts from the Nmap Scripting Engine (NSE) to fetch web titles, SSL certs, and SMB shares.
* **`-O`**: **OS Detection** — Analyzes TCP packet headers to guess the operating system.

---

## 5. Nmap Scripting Engine (NSE) Power

Nmap is not just a port scanner; it has over **600 built-in scripts** categorized into:
* `default`: Fast, safe reconnaissance scripts (`-sC`).
* `vuln`: Checks if services have famous known CVE vulnerabilities (`--script vuln`).
* `safe`: Scripts guaranteed not to crash the target service.
* `discovery`: Queries Active Directory, DNS, database instances, and network shares.

**Example Vulnerability Scan:**
```bash
nmap -p 80,443 --script vuln <target-ip>
```

---

## 6. Official Safe Target: `scanme.nmap.org`

> [!IMPORTANT]
> The creators of Nmap set up a dedicated public server specifically so students and security researchers can legally practice running Nmap:
> **Target:** `scanme.nmap.org`
> *(Never scan external businesses or schools without authorization).*
