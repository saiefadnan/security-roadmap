# 🟡 Phase 4 — Practical Ethical Hacking

> **Goal:** Master practical attack techniques: Reconnaissance, Active Enumeration, Web Security, Vulnerability Assessment, and Exploitation Tooling.

---

## 🗺️ Roadmap Modules & Guides

1. **[01-passive-reconnaissance-and-osint.md](01-passive-reconnaissance-and-osint.md)**
   - Passive vs. Active reconnaissance.
   - Google Dorking operators & high-value search queries.
   - Shodan banner intelligence & device discovery.
   - Domain & Certificate Transparency OSINT.

2. **[02-active-enumeration-and-nmap.md](02-active-enumeration-and-nmap.md)**
   - Port scanning mechanics (TCP Connect, SYN Stealth, UDP).
   - Port states: open, closed, filtered.
   - 4-stage professional scanning methodology.
   - Service version detection (`-sV`) & OS fingerprinting (`-O`).
   - Nmap Scripting Engine (NSE) for vulnerability discovery.
3. **[03-web-directory-and-parameter-fuzzing.md](03-web-directory-and-parameter-fuzzing.md)**
   - Unlinked endpoints & hidden file discovery.
   - HTTP status code interpretation (200, 301, 401, 403, 404).
   - Gobuster & ffuf command syntax & usage.
   - SecLists & curated wordlist utilization.
4. **[04-owasp-top-10-fundamentals.md](04-owasp-top-10-fundamentals.md)**
   - The Big 4 Web Attacks: SQLi, Broken Access/IDOR, XSS, CSRF.
   - Root causes, attack flows, and real-world payload examples.
   - Developer defensive controls (Prepared Statements, Output Encoding, Anti-CSRF Tokens).
   - Free legal training labs (PortSwigger Academy, Juice Shop, DVWA).
5. **[05-network-security-weak-protocols.md](05-network-security-weak-protocols.md)**
   - The Big 5 Weak Protocols: FTP, Telnet, SSH, SMB, SNMP.
   - Cleartext credentials, anonymous FTP logins, Telnet sniffing.
   - SSH password spraying with Hydra & key security.
   - SMB null sessions & EternalBlue (MS17-010) overview.
   - SNMP community strings (`public`/`private`) & information leakage.
6. **[06-vulnerability-assessment-and-metasploit.md](06-vulnerability-assessment-and-metasploit.md)**
   - Vulnerability Assessment vs. Exploitation & CVSS scoring.
   - Metasploit Framework modular architecture (exploits, payloads, auxiliary, post).
   - Staged vs. Inline payloads & Reverse vs. Bind shells.
   - In-memory Meterpreter capabilities (sysinfo, migrate, hashdump).
   - The 6-step exploitation workflow and session management.
7. **[07-password-attacks-and-cracking-mechanics.md](07-password-attacks-and-cracking-mechanics.md)**
   - Online attacks (Hydra) vs. Offline attacks (Hashcat, John the Ripper).
   - Cryptographic hashing mechanics, salts, and rainbow tables.
   - OS Hash formats: Windows NTLM, Linux `/etc/shadow` ($6$, $y$), and web hashes (bcrypt, Argon2).
   - John the Ripper (`unshadow`, file format extractors) & Hashcat GPU modes (`-m 1000`, `-a 0`, `-a 3`).
   - Mutation rules and defensive passphrase policies.
8. **[08-malware-and-social-engineering-concepts.md](08-malware-and-social-engineering-concepts.md)**
   - Malware taxonomy: Droppers/Loaders, Ransomware hybrid encryption, InfoStealers, Rootkits.
   - Command & Control (C2) architecture: Beacons, sleeping & jitter, malleable profiles.
   - Social engineering vectors: Spear phishing, Whaling, Vishing, Baiting.
   - Modern AiTM credential harvesting (Evilginx2) & EDR telemetry alarms.
9. **[09-pentest-methodology-and-reporting.md](09-pentest-methodology-and-reporting.md)**
55:    - The 7-stage PTES framework (Pre-engagement to Reporting).
56:    - Scoping models: Black Box, Grey Box, White Box.
57:    - Legal pillars: SOW, NDA, and Letter of Authorization (LoA).
58:    - Executive Summary vs. Technical Report structure.
59:    - Anatomy of a world-class vulnerability finding (CVSS, PoC, Business Impact, Code Remediation).
60: 
61: ---
62: 
63: ## 🖼️ Educational Visual Diagrams
64: 1. **[01-nmap-mastery-card.jpg](images/01-nmap-mastery-card.jpg)** — Algomaster visual cheat sheet covering TCP handshake scanning (-sT vs -sS), the 3 port states, 4-stage methodology, and core flags.
65: 2. **[02-web-fuzzing-card.jpg](images/02-web-fuzzing-card.jpg)** — Algomaster visual cheat sheet covering directory fuzzing, HTTP status codes, the 4 ffuf filtering flags (-fs, -fc, -fw, -fl), and command comparisons.
66: 3. **[03-gobuster-mastery-card.jpg](images/03-gobuster-mastery-card.jpg)** — Algomaster visual cheat sheet covering Gobuster's 3 operational modes (dir, dns, vhost), flag syntax, status codes, and progressive workflow.
67: 4. **[04-owasp-top-10-card.jpg](images/04-owasp-top-10-card.jpg)** — Algomaster visual cheat sheet covering the Big 4 web attack mechanics (SQLi, XSS, IDOR, CSRF), severity matrix, and developer defenses.
68: 5. **[05-weak-protocols-card.jpg](images/05-weak-protocols-card.jpg)** — Algomaster visual cheat sheet covering FTP/Telnet plaintext flaws, SMB null sessions, SSH Hydra spraying, and SNMP community strings.
69: 6. **[06-metasploit-mastery-card.jpg](images/06-metasploit-mastery-card.jpg)** — Algomaster visual cheat sheet covering Metasploit core modules, staged vs inline payloads, the 6-step attack workflow, and Meterpreter essentials.
70: 7. **[07-password-cracking-card.jpg](images/07-password-cracking-card.jpg)** — Algomaster visual cheat sheet covering Online vs Offline attacks, common hash formats (NTLM, shadow, bcrypt), John & Hashcat syntax, and cracking attack modes.
71: 8. **[08-malware-and-social-engineering-card.jpg](images/08-malware-and-social-engineering-card.jpg)** — Algomaster visual cheat sheet covering malware taxonomy (Ransomware, Stealers, Rootkits), C2 beacon lifecycle, phishing vectors, and EDR detection.
72: 9. **[09-pentest-methodology-card.jpg](images/09-pentest-methodology-card.jpg)** — Algomaster visual cheat sheet covering the 7 PTES stages, Black/Grey/White scoping models, vulnerability finding anatomy, and Executive vs Technical reports.
