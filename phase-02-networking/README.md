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

4. **[04-http-https-and-tls.md](file:///e:/my_projects/hack/phase-02-networking/04-http-https-and-tls.md)**
   - Plaintext HTTP (Port 80) risks & session cookie theft.
   - The TLS 1.3 Handshake flow: Client Hello, Server Hello, Key Shares, and Session Keys.
   - Real terminal inspection using `curl -v -I`.
   - Deconstructing Cipher Suites (`TLS_AES_256_GCM_SHA384`).
   - Certificate Authority (CA) chain of trust and why MITM attacks trigger browser certificate warnings.

5. **[05-vlans-and-segmentation.md](file:///e:/my_projects/hack/phase-02-networking/05-vlans-and-segmentation.md)**
   - Broadcast domain isolation & corporate network tiering.
   - Access Ports vs. Trunk Ports.
   - 802.1Q Tagging packet journey (TPID 0x8100, VLAN IDs 1-4094).
   - Offensive security: Switch Spoofing (DTP exploitation) & Double Tagging (Native VLAN hop).

6. **[06-vpns-and-tunneling.md](file:///e:/my_projects/hack/phase-02-networking/06-vpns-and-tunneling.md)**
   - Problem solved: remote private LAN access across untrusted public networks.
   - Kernel virtual adapters (`tun0`, `wg0`).
   - 3-step packet encapsulation flow: Inner private packet $\rightarrow$ Outer encrypted UDP envelope $\rightarrow$ Gateway decapsulation.
   - WireGuard vs. OpenVPN vs. IPsec.
   - Red team angles: Full vs. Split tunneling pivot host risks, exposed VPN gateways.

7. **[07-firewalls-and-proxies.md](file:///e:/my_projects/hack/phase-02-networking/07-firewalls-and-proxies.md)**
   - Stateless vs. Stateful Packet Inspection vs. Web Application Firewalls (WAF).
   - Linux kernel `iptables` chains: `INPUT`, `OUTPUT`, and `FORWARD`.
   - Recon implications: `DROP` (Filtered / timeout) vs. `REJECT` (Closed / reset).
   - Forward Proxy (protects client identity) vs. Reverse Proxy (protects server architecture).
   - Burp Suite intercepting proxy & SOCKS5 pivoting (`proxychains`).

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
- `08-http-https-tls-handshake.jpg`: 3-card breakdown of HTTP vs. HTTPS, the TLS 1.3 Handshake, and AES-256-GCM encryption.
- `09-why-ssl-certificate.jpg`: 3-card breakdown explaining why a naked public key is vulnerable to MITM and how the CA signed certificate binds domain identity to the public key.
- `10-vlan-8021q-tagging-flow.jpg`: 3-card sequential packet flow of Ingress on Access Port, 4-byte 802.1Q Tag insertion across Trunk link, and Egress Tag stripping.
- `11-vpn-tunnel-encapsulation-flow.jpg`: 3-card sequential packet flow of Inner private packet creation (tun0), Outer UDP envelope encryption in transit, and Gateway decapsulation into office LAN.
- `12-proxy-architectures-flow.jpg`: 3-card comparison of Forward Proxy (client shield), Reverse Proxy (server shield), and Intercepting Proxy (Burp Suite).



