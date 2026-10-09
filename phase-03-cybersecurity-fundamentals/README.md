# 🟡 Phase 3 — Cybersecurity Fundamentals

> **Goal:** Master core security models, offensive terminology, adversary methodologies, and defensive controls before hands-on exploitation.

---

## 🗺️ Roadmap Modules & Guides

1. **[01-cia-triad-and-security-principles.md](01-cia-triad-and-security-principles.md)**
   - The CIA Triad: Confidentiality, Integrity, Availability.
   - Offensive attack vectors mapped to each pillar.
   - The extended model: Authentication, Authorization, Non-Repudiation, Accountability.

2. **[02-threat-modeling-and-attack-surface.md](02-threat-modeling-and-attack-surface.md)**
   - Attack Surface definition: Network, Software, Human.
   - Microsoft STRIDE threat classification model.
   - Risk scoring with DREAD.

3. **[03-vulnerability-exploit-payload.md](03-vulnerability-exploit-payload.md)**
   - The Holy Trinity: Vulnerability, Exploit, Payload.
   - Bind Shell vs. Reverse Shell mechanics (firewall traversal).
   - Zero-Day (0-Day) vs. N-Day vulnerabilities.

4. **[04-auth-and-cryptography.md](04-auth-and-cryptography.md)**
   - Authentication (AuthN) vs. Authorization (AuthZ).
   - Encryption (Two-way) vs. Hashing (One-way).
   - Salting, rainbow tables, and password cracking mechanics.

5. **[05-cve-and-cvss.md](05-cve-and-cvss.md)**
   - CVE naming conventions and landmark examples (EternalBlue, Log4Shell).
   - CVSS scoring tiers (Low, Medium, High, Critical).
   - Base metric breakdown (AV, AC, PR, UI, and CIA impact).

6. **[06-defensive-controls-ids-ips-siem.md](06-defensive-controls-ids-ips-siem.md)**
   - Preventive vs. Detective vs. Corrective security controls.
   - IDS (passive alert) vs. IPS (in-line active block).
   - SIEM log aggregation, correlation engines, and SOC alerting.

7. **[07-adversary-attack-lifecycle.md](07-adversary-attack-lifecycle.md)**
   - The 10-Stage Cyber Attack Lifecycle (Cyber Kill Chain).
   - Infiltration (Recon, Enumeration, Initial Access).
   - Foothold & Escalation (Execution, Privilege Escalation).
   - Expansion & Objective (Discovery, Lateral Movement, Actions on Objective).
   - Defensive Response (Detection, Remediation).

---

## 🖼️ Educational Visual Diagrams
All architecture diagrams and mental models for Phase 3 are stored in [`images/`](images/):
- `01-attack-lifecycle-flow.jpg`: 4-block modular flow diagram of the 10-Stage Adversary Attack Lifecycle.

