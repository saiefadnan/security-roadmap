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
5. *(Upcoming)* **Network Security: Exploiting Weak Protocols**
6. *(Upcoming)* **Vulnerability Assessment & Metasploit Framework**
7. *(Upcoming)* **Password Attacks & Cracking Mechanics**
8. *(Upcoming)* **Malware & Social Engineering Concepts**
9. *(Upcoming)* **Professional Penetration Testing Methodology**

---

## 🖼️ Educational Visual Diagrams
1. **[01-nmap-mastery-card.jpg](images/01-nmap-mastery-card.jpg)** — Algomaster visual cheat sheet covering TCP handshake scanning (-sT vs -sS), the 3 port states, 4-stage methodology, and core flags.
2. **[02-web-fuzzing-card.jpg](images/02-web-fuzzing-card.jpg)** — Algomaster visual cheat sheet covering directory fuzzing, HTTP status codes, the 4 ffuf filtering flags (-fs, -fc, -fw, -fl), and command comparisons.
3. **[03-gobuster-mastery-card.jpg](images/03-gobuster-mastery-card.jpg)** — Algomaster visual cheat sheet covering Gobuster's 3 operational modes (dir, dns, vhost), flag syntax, status codes, and progressive workflow.
4. **[04-owasp-top-10-card.jpg](images/04-owasp-top-10-card.jpg)** — Algomaster visual cheat sheet covering the Big 4 web attack mechanics (SQLi, XSS, IDOR, CSRF), severity matrix, and developer defenses.
