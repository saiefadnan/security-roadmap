# 🟢 Phase 2 — Networking: On The Wire

> **Goal:** Understand what is actually happening on the physical and virtual wire at the packet level.

---

## 🗺️ Roadmap Modules & Guides

1. **[01-tcp-udp-and-handshake.md](file:///e:/my_projects/hack/phase-02-networking/01-tcp-udp-and-handshake.md)**
   - TCP vs. UDP core differences.
   - The 3-Way Handshake (`SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`).
   - The 3-card TCP conversation lifecycle (Handshake, PUSH data transfer, FIN teardown).
   - Core TCP flags (`[S]`, `[.]`, `[P]`, `[F]`, `[R]`).
   - Live packet capture breakdown using `tcpdump`.
   - Security mechanics: SYN Floods, Nmap Stealth Scans (`-sS`), and Port states (OPEN, CLOSED, FILTERED).

2. **[02-dhcp-and-dns.md](file:///e:/my_projects/hack/phase-02-networking/02-dhcp-and-dns.md)**
   - Device auto-configuration via DHCP DORA flow (`Discover`, `Offer`, `Request`, `ACK`).
   - Offensive risks: Rogue DHCP Servers (instant MITM) and DHCP Starvation attacks.
   - Core DNS Record types (`A`, `AAAA`, `CNAME`, `MX`, `TXT`, `NS`).
   - Live DNS enumeration & vendor reconnaissance with `dig`.

3. **[03-arp-routing-and-nat.md](file:///e:/my_projects/hack/phase-02-networking/03-arp-routing-and-nat.md)**
   - The complete 4-stage packet journey from Laptop to Router to Google and back.
   - Layer 2 (MAC) vs. Layer 3 (IP) encapsulation mechanics.
   - Router NAT translation table tracking.
   - ARP poisoning vulnerability & MITM mechanics.

---

## 🖼️ Educational Visual Cards
All architecture diagrams and visual cards for this phase are organized in the [`images/`](file:///e:/my_projects/hack/phase-02-networking/images) directory:
- `01-tcp-3-way-handshake.jpg`: Glowing flow diagram of client-server synchronization.
- `02-tcp-lifecycle-cards.jpg`: 3-card modular flow of Handshake, Data Transfer (PUSH), and Teardown (FIN).
- `03-dhcp-dora-process.jpg`: 4-card sequence of the DHCP DORA leasing cycle.
- `04-dns-record-types.jpg`: 6-card modular grid of Core DNS Record types and security recon.
- `05-email-spoofing-spf.jpg`: 3-card breakdown of Email Spoofing and SPF DNS validation.
- `06-email-relay-flow.jpg`: 3-card sequence showing why normal users' emails pass SPF via Google's relay.
- `07-arp-routing-nat-flow.jpg`: 4-card complete packet journey across ARP, the Router envelope, NAT, and return delivery.
