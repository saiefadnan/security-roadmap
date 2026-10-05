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

---

## 🖼️ Educational Visual Cards
All architecture diagrams and visual cards for this phase are organized in the [`images/`](file:///e:/my_projects/hack/phase-02-networking/images) directory:
- `01-tcp-3-way-handshake.jpg`: Glowing flow diagram of client-server synchronization.
- `02-tcp-lifecycle-cards.jpg`: 3-card modular flow of Handshake, Data Transfer (PUSH), and Teardown (FIN).
