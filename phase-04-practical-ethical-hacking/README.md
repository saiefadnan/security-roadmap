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
37: 6. **[06-vulnerability-assessment-and-metasploit.md](06-vulnerability-assessment-and-metasploit.md)**
38:    - Vulnerability Assessment vs. Exploitation & CVSS scoring.
39:    - Metasploit Framework modular architecture (exploits, payloads, auxiliary, post).
40:    - Staged vs. Inline payloads & Reverse vs. Bind shells.
41:    - In-memory Meterpreter capabilities (sysinfo, migrate, hashdump).
42:    - The 6-step exploitation workflow and session management.
43: 7. *(Upcoming)* **Password Attacks & Cracking Mechanics**
44: 8. *(Upcoming)* **Malware & Social Engineering Concepts**
45: 9. *(Upcoming)* **Professional Penetration Testing Methodology**
46: 
47: ---
48: 
49: ## 🖼️ Educational Visual Diagrams
50: 1. **[01-nmap-mastery-card.jpg](images/01-nmap-mastery-card.jpg)** — Algomaster visual cheat sheet covering TCP handshake scanning (-sT vs -sS), the 3 port states, 4-stage methodology, and core flags.
51: 2. **[02-web-fuzzing-card.jpg](images/02-web-fuzzing-card.jpg)** — Algomaster visual cheat sheet covering directory fuzzing, HTTP status codes, the 4 ffuf filtering flags (-fs, -fc, -fw, -fl), and command comparisons.
52: 3. **[03-gobuster-mastery-card.jpg](images/03-gobuster-mastery-card.jpg)** — Algomaster visual cheat sheet covering Gobuster's 3 operational modes (dir, dns, vhost), flag syntax, status codes, and progressive workflow.
53: 4. **[04-owasp-top-10-card.jpg](images/04-owasp-top-10-card.jpg)** — Algomaster visual cheat sheet covering the Big 4 web attack mechanics (SQLi, XSS, IDOR, CSRF), severity matrix, and developer defenses.
54: 5. **[05-weak-protocols-card.jpg](images/05-weak-protocols-card.jpg)** — Algomaster visual cheat sheet covering FTP/Telnet plaintext flaws, SMB null sessions, SSH Hydra spraying, and SNMP community strings.
55: 6. **[06-metasploit-mastery-card.jpg](images/06-metasploit-mastery-card.jpg)** — Algomaster visual cheat sheet covering Metasploit core modules, staged vs inline payloads, the 6-step attack workflow, and Meterpreter essentials.
