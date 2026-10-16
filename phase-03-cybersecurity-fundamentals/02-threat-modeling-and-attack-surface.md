# 🎯 Step 2: Threat Modeling & Attack Surface

> **Phase 3: Cybersecurity Fundamentals**  
> *"If you don't map your own attack surface, adversaries will map it for you."*

---

## 1. What is an Attack Surface?

An **Attack Surface** is the sum total of all attack vectors (entry points) where an unauthorized entity can enter, interact with, or extract data from a system.

### The 3 Core Attack Surfaces:
1. **Network Attack Surface:**
   - Every listening port (`ss -tuln`, Nmap).
   - Protocols running on the wire (SSH, HTTP, SMB, DNS).
   - Remote access services (VPN gateways, RDP).
2. **Software & Application Attack Surface:**
   - Web application forms, input fields, search bars.
   - API endpoints (`/api/v1/auth`, `/upload`).
   - Third-party open-source libraries and package dependencies.
3. **Human / Physical Attack Surface:**
   - Employees vulnerable to phishing, social engineering, or pretexting.
   - Physical USB ports, rogue Ethernet wall jacks, discarded printed documents.

> **💡 Golden Rule of Defense:**  
> **Attack Surface Reduction (ASR):** Closing unused ports, disabling unneeded services, restricting root SSH, and applying least privilege.

---

## 2. Threat Modeling & The STRIDE Framework

Threat modeling is the proactive process of identifying assets, threats, vulnerabilities, and mitigations before systems are deployed.

### The Microsoft STRIDE Framework

| Threat | Definition | CIA Pillar Violated | Example Attack |
| :--- | :--- | :--- | :--- |
| **S — Spoofing** | Faking identity to gain access. | **Authentication** | IP spoofing, email spoofing, stolen session tokens. |
| **T — Tampering** | Unauthorized modification of data. | **Integrity** | MITM packet modification, parameter tampering (`price=1`). |
| **R — Repudiation** | Denying an action took place due to poor logging. | **Non-Repudiation** | Performing transactions on systems with no audit trail. |
| **I — Information Disclosure** | Exposing private data to unauthorized eyes. | **Confidentiality** | SQL injection dumping databases, packet sniffing. |
| **D — Denial of Service** | Crashing or degrading availability. | **Availability** | SYN floods, DDoS, CPU exhaustion loops. |
| **E — Elevation of Privilege** | Gaining unauthorized higher privileges. | **Authorization** | Linux SUID binary abuse, Windows token manipulation. |

---

## 3. Threat Assessment Methodologies (DREAD & PASTA)

Security teams prioritize threats using scoring models like **DREAD**:
- **D**amage potential: How severe is the impact?
- **R**eproducibility: How easily can the attack be duplicated?
- **E**xploitability: How much skill is needed?
- **A**ffected users: How many people are impacted?
- **D**iscoverability: How easy is it for an adversary to find?
