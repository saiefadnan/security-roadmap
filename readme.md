# 🔴 Red Team & Offensive Security Roadmap

> **Goal:** Become capable of performing authorized penetration tests, simulating adversary behavior in isolated labs, analyzing attacks, and building original offensive-security projects.

**Core loop:**

```text
Learn → Lab → Attack → Analyze → Detect → Build → Document
```

---

# 🗺️ Roadmap

```text
                    FOUNDATION
                        │
             ┌──────────┴──────────┐
             ↓                     ↓
          Linux               Networking
             └──────────┬──────────┘
                        ↓
               Security Fundamentals
                        ↓
                 Pentesting Basics
                        ↓
              ┌─────────┴─────────┐
              ↓                   ↓
         Web Security        Linux Security
              │
              └─────────┬─────────┘
                        ↓
                Windows Fundamentals
                        ↓
               Active Directory
                        ↓
                 Red Teaming
                        ↓
              Attack Simulation Lab
                        ↓
               Security Projects
                        ↓
             ┌──────────┼──────────┐
             ↓          ↓          ↓
            AD         Web       Cloud
             │
             └──────────┬──────────┐
                        ↓
                  Specialization
             ┌──────────┼──────────┐
             ↓          ↓          ↓
          Telecom    Exploit Dev   AI Security
```

---

# 🟢 PHASE 0 — Setup Your Security Lab

**Goal:** Have a safe environment before learning offensive techniques.

## Install / prepare

- [x] WSL2 Ubuntu
- [ ] VirtualBox / VMware / Hyper-V
- [x] Git
- [x] Python
- [x] VS Code
- [ ] Wireshark
- [ ] Burp Suite
- [ ] Docker

Later:

- [ ] Kali Linux VM
- [ ] Windows Server VM
- [ ] Windows client VM
- [ ] Vulnerable Linux VM
- [ ] Vulnerable web applications

## Basic lab architecture

```text
                    Windows Host
                         │
                ┌────────┴────────┐
                │  Hypervisor     │
                └────────┬────────┘
                         │
                 Isolated Lab LAN
                         │
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
    Kali Linux       Linux Server     Windows PC
                                       │
                                  Domain Controller
```

> Keep offensive experiments isolated to systems you own or have explicit permission to test.

---

# 🟢 PHASE 1 — Linux Fundamentals

**Goal:** Become comfortable working from a Linux terminal.

### Learn

- [x] Filesystem
- [x] Users and groups
- [x] File permissions
- [x] Processes
- [x] Services
- [x] SSH
- [x] Environment variables
- [x] Package management
- [x] Logs
- [x] Networking commands
- [x] Bash scripting

### Commands

```text
ls
cd
pwd
cp
mv
rm
cat
less
grep
find
chmod
chown
ps
top
ss
ip
curl
wget
ssh
```

### Learn Bash

Build small scripts that:

- [x] Parse files
- [x] Search logs
- [x] Check services
- [x] Process command output
- [x] Automate repetitive tasks

### 🧪 Mini Projects

**Linux Log Analyzer** ([Folder](file:///e:/my_projects/hack/phase-01-linux-fundamentals/03-mini-projects/log-analyzer))

```text
auth.log
    ↓
Python/Bash
    ↓
Find suspicious events
    ↓
Generate report
```

**Network Information Tool** ([Folder](file:///e:/my_projects/hack/phase-01-linux-fundamentals/03-mini-projects/net-info-tool))

```text
Interface
IP
Gateway
DNS
Open connections
```

---

# 🟢 PHASE 2 — Networking

**Goal:** Understand what is actually happening on the wire.

### Learn

- [ ] IPv4
- [ ] IPv6 basics
- [ ] Subnetting
- [ ] MAC addresses
- [ ] ARP
- [ ] TCP
- [ ] UDP
- [ ] TCP handshake
- [ ] TCP flags
- [ ] DNS
- [ ] DHCP
- [ ] HTTP
- [ ] HTTPS
- [ ] TLS
- [ ] NAT
- [ ] Routing
- [ ] VLANs
- [ ] VPNs
- [ ] Firewalls
- [ ] Proxies

### Tools

- [ ] Wireshark
- [ ] Nmap
- [ ] Netcat
- [ ] curl
- [ ] dig
- [ ] traceroute

### 🧪 Project #1 — Network Traffic Analyzer

Capture traffic from your own lab.

Build a small Python tool that extracts:

```text
Source IP
Destination IP
Protocol
Port
Packet count
DNS queries
HTTP requests
```

Then visualize the results.

---

# 🟡 PHASE 3 — Cybersecurity Fundamentals

**Goal:** Understand security concepts before jumping into exploitation.

### Learn

- [ ] CIA triad
- [ ] Threat modeling
- [ ] Attack surface
- [ ] Vulnerability
- [ ] Exploit
- [ ] Payload
- [ ] Authentication
- [ ] Authorization
- [ ] Encryption
- [ ] Hashing
- [ ] CVE
- [ ] CVSS
- [ ] Security controls
- [ ] IDS
- [ ] IPS
- [ ] SIEM

### Understand the attack lifecycle

```text
Recon
 ↓
Enumeration
 ↓
Initial Access
 ↓
Execution
 ↓
Privilege Escalation
 ↓
Discovery
 ↓
Lateral Movement
 ↓
Objective
 ↓
Detection
 ↓
Remediation
```

---

# 🟡 PHASE 4 — Hacking Ki Series

**Goal:** Get your first broad exposure to practical ethical hacking.

Work through the relevant topics instead of treating it as a passive video course.

### Focus on

- [ ] Reconnaissance
- [ ] Enumeration
- [ ] Linux security
- [ ] Web security
- [ ] Network security
- [ ] Vulnerability assessment
- [ ] Basic exploitation
- [ ] Password security
- [ ] Social engineering concepts
- [ ] Malware concepts
- [ ] Pentesting methodology

### Tools

- [ ] Nmap
- [ ] Burp Suite
- [ ] Metasploit
- [ ] Wireshark
- [ ] Gobuster
- [ ] ffuf
- [ ] Netcat

### Reference

**Red Team Roadmap**

Use it to see what topics come after the fundamentals rather than trying to learn everything immediately.

---

# 🟡 PHASE 5 — Pentesting Fundamentals

**Goal:** Learn how a professional penetration test is structured.

### Methodology

```text
1. Scope
   ↓
2. Reconnaissance
   ↓
3. Enumeration
   ↓
4. Vulnerability Identification
   ↓
5. Validation
   ↓
6. Exploitation
   ↓
7. Privilege Escalation
   ↓
8. Evidence Collection
   ↓
9. Reporting
   ↓
10. Remediation
```

### Learn

- [ ] Information gathering
- [ ] Service enumeration
- [ ] Vulnerability identification
- [ ] Exploitation fundamentals
- [ ] Linux privilege escalation
- [ ] Windows privilege escalation
- [ ] Credential security
- [ ] Basic post-exploitation concepts
- [ ] Reporting

### 🧪 Project #2 — Mini Pentest

Create a small vulnerable lab.

```text
Kali
  │
  ↓
Target Linux VM
  │
  ├── Web service
  ├── SSH
  └── Database
```

Produce a professional report:

```text
Executive Summary
Scope
Methodology
Findings
Evidence
Impact
Risk
Remediation
Conclusion
```

---

# 🟠 PHASE 6 — Web Application Security

**Goal:** Become strong at web/API security.

This is especially useful given your full-stack development background.

## Learn HTTP deeply

- [ ] Requests
- [ ] Responses
- [ ] Headers
- [ ] Cookies
- [ ] Sessions
- [ ] Authentication
- [ ] Authorization
- [ ] APIs
- [ ] CORS
- [ ] JWT
- [ ] OAuth/OIDC basics

## OWASP-style vulnerabilities

Learn and practice:

- [ ] SQL Injection
- [ ] XSS
- [ ] CSRF
- [ ] IDOR / authorization flaws
- [ ] SSRF
- [ ] Command injection
- [ ] File inclusion
- [ ] File upload vulnerabilities
- [ ] Authentication flaws
- [ ] Session flaws
- [ ] API vulnerabilities
- [ ] Business-logic vulnerabilities

## Labs

- [ ] PortSwigger Web Security Academy
- [ ] OWASP Juice Shop
- [ ] DVWA
- [ ] WebGoat

## Tools

- [ ] Burp Suite
- [ ] curl
- [ ] ffuf
- [ ] Nmap

### 🧪 Project #3 — Vulnerable Web Application

Build:

```text
Next.js
   ↓
Node / Express
   ↓
PostgreSQL
```

Create intentionally vulnerable lab endpoints.

For every vulnerability document:

```text
Vulnerability
      ↓
Root Cause
      ↓
Lab Reproduction
      ↓
Impact
      ↓
Detection
      ↓
Fix
      ↓
Regression Test
```

---

# 🟠 PHASE 7 — Linux Privilege Escalation

**Goal:** Understand how local privilege boundaries fail.

### Learn concepts

- [ ] Linux permissions
- [ ] SUID/SGID
- [ ] sudo configuration
- [ ] Services
- [ ] Cron
- [ ] Environment variables
- [ ] PATH issues
- [ ] File permissions
- [ ] Capabilities
- [ ] Kernel/security boundaries

### References

- **GTFOBins**
- **PEASS-ng**
- **HackTricks**

Use them as references while working through labs.

### 🧪 Project #4 — Privilege Escalation Lab

Create several intentionally misconfigured Linux environments and write a guide showing:

```text
Initial User
     ↓
Enumeration
     ↓
Misconfiguration
     ↓
Privilege Boundary
     ↓
Root
     ↓
Remediation
```

---

# 🟠 PHASE 8 — Windows Fundamentals

**Goal:** Understand Windows before attacking Active Directory.

### Learn

- [ ] Windows filesystem
- [ ] Users/groups
- [ ] Processes
- [ ] Services
- [ ] Registry
- [ ] PowerShell
- [ ] Windows permissions
- [ ] Event Viewer
- [ ] Windows authentication
- [ ] SMB
- [ ] RDP
- [ ] Windows networking

### PowerShell

Learn enough to:

- [ ] Query system information
- [ ] Manage processes
- [ ] Search files
- [ ] Parse logs
- [ ] Automate administration
- [ ] Query Windows security information

---

# 🔴 PHASE 9 — Active Directory

**Goal:** Build the foundation for enterprise red teaming.

## Learn AD

- [ ] Domains
- [ ] Domain Controllers
- [ ] Users
- [ ] Groups
- [ ] OUs
- [ ] Group Policy
- [ ] LDAP
- [ ] Kerberos
- [ ] NTLM
- [ ] SMB
- [ ] DNS
- [ ] Service accounts
- [ ] ACLs
- [ ] Delegation

### Build the lab

```text
                 Kali
                   │
             Isolated LAN
                   │
          ┌────────┴────────┐
          ↓                 ↓
     Domain Controller   Windows Client
          │
     ┌────┴────┐
     ↓         ↓
   User A    User B
```

### Study attack concepts in the lab

- [ ] Credential exposure
- [ ] Password security
- [ ] Kerberos abuse concepts
- [ ] Permission/ACL weaknesses
- [ ] Service misconfigurations
- [ ] Privilege escalation
- [ ] Lateral movement
- [ ] Domain privilege escalation
- [ ] Persistence concepts

### References

- **ActiveDirectory-Pentest-Resources**
- **Active Directory Pentesting**
- **GOAD**
- **HackTricks**
- **Impacket**

### 🧪 Project #5 — AD Attack & Detection Lab

Create an attack scenario and document:

```text
Initial foothold
      ↓
Enumeration
      ↓
Privilege escalation
      ↓
Credential discovery
      ↓
Lateral movement
      ↓
Domain objective
```

Then investigate the same activity from the defender side.

---

# 🔴 PHASE 10 — Red Teaming

**Goal:** Understand adversary simulation as a complete operation.

## Study MITRE ATT&CK

Learn:

- [ ] Tactics
- [ ] Techniques
- [ ] Sub-techniques
- [ ] Detection
- [ ] Mitigation
- [ ] Procedure examples

Map every major lab exercise to ATT&CK.

```text
ATT&CK Technique
       ↓
Lab Simulation
       ↓
Telemetry
       ↓
Detection
       ↓
Mitigation
```

## Red Team Lifecycle

```text
Recon
 ↓
Initial Access
 ↓
Execution
 ↓
Privilege Escalation
 ↓
Persistence
 ↓
Discovery
 ↓
Lateral Movement
 ↓
Objective
 ↓
Evidence
 ↓
Report
```

---

# 🔴 PHASE 11 — Detection Engineering

**Goal:** Understand what happens after an attack.

### Learn

- [ ] Windows Event Logs
- [ ] Sysmon
- [ ] Linux logs
- [ ] Network telemetry
- [ ] Authentication logs
- [ ] PowerShell logging
- [ ] SIEM concepts
- [ ] Detection rules
- [ ] False positives
- [ ] Incident investigation

### Tools

- [ ] Sysmon
- [ ] Wazuh
- [ ] ELK
- [ ] Wireshark

### 🧪 Project #6 — Attack Detection Lab

```text
Red Team Activity
       ↓
System / Network Telemetry
       ↓
SIEM
       ↓
Detection Rule
       ↓
Alert
       ↓
Investigation
       ↓
Mitigation
```

The project should demonstrate both:

**Offensive:** What happened?

**Defensive:** How could we detect it?

---

# 🔥 PHASE 12 — Build Security Tools

Now start writing your own tools.

## Project #7 — Automated Recon Tool

```text
Target
  ↓
Host Discovery
  ↓
Port Scan
  ↓
Service Detection
  ↓
HTTP Enumeration
  ↓
Technology Detection
  ↓
Correlation
  ↓
Report
```

Possible stack:

```text
Python
Nmap
Requests
SQLite/PostgreSQL
Rich / Typer
```

Add your own analysis rather than simply wrapping another tool.

---

# 🔥 PHASE 13 — Vulnerability Scanner

## Project #8

Build a lab-focused vulnerability scanner.

Example:

```text
http://lab.local
```

Output:

```text
[+] HTTP detected
[+] Login endpoint found
[!] Missing security header
[!] Potential authorization issue
[!] Interesting API endpoint
```

Use a finding pipeline:

```text
Potential Finding
       ↓
Validation
       ↓
Confirmed Finding
       ↓
Evidence
       ↓
Report
```

This helps reduce false positives.

---

# 🔥 PHASE 14 — Build a Mini CTF Platform

## Project #9

Build your own small CTF platform.

### Features

- [ ] Authentication
- [ ] Challenges
- [ ] Vulnerable applications
- [ ] Flags
- [ ] Scoring
- [ ] Leaderboard
- [ ] Writeups
- [ ] Admin dashboard

### Architecture

```text
Frontend
   ↓
API
   ↓
Database
   ↓
Challenge Infrastructure
```

This combines:

**Full-stack development + cybersecurity.**

---

# 📡 PHASE 15 — Telecom Security

> This is an optional specialization after the core red-team foundation.

Given an interest in SS7, build a **toy telecom signaling environment**, not a connection to real carrier infrastructure.

## Learn

- [ ] SS7 architecture
- [ ] SIGTRAN
- [ ] SCCP
- [ ] TCAP
- [ ] MAP
- [ ] HLR/VLR concepts
- [ ] Diameter
- [ ] LTE/5G core concepts
- [ ] Telecom signaling security

### 🧪 Project #10 — Telecom Security Simulator

```text
Subscriber Simulator
        ↓
MSC Simulator
        ↓
      SCCP
        ↓
      TCAP
        ↓
       MAP
        ↓
HLR Simulator
```

Add:

```text
Signaling Firewall
       ↓
Rules
       ↓
Anomaly Detection
       ↓
ALERT / BLOCK
```

### Project objective

Show:

```text
Normal Signaling
       vs
Suspicious Signaling
       ↓
Detection
       ↓
Decision
       ↓
Alert / Block
```

---

# ⚙️ PHASE 16 — Advanced Exploit Development

**Do this after the fundamentals.**

### Learn

- [ ] C
- [ ] Assembly
- [ ] Memory layout
- [ ] Stack
- [ ] Heap
- [ ] Processes
- [ ] Debugging
- [ ] Memory corruption concepts
- [ ] Exploit mitigations
- [ ] Reverse engineering

Eventually explore:

- GDB
- x86/x64 assembly
- WinDbg
- Ghidra
- Binary analysis

Keep initial exploitation practice inside intentionally vulnerable binaries and isolated labs.

---

# 🤖 PHASE 17 — AI Security / Red Teaming

Optional specialization after core offensive skills.

### Learn

- [ ] LLM architecture
- [ ] Prompt injection
- [ ] Tool/plugin security
- [ ] Agent security
- [ ] Data leakage
- [ ] Model security
- [ ] AI application security

### Project idea

Build an intentionally vulnerable AI agent:

```text
User
 ↓
AI Agent
 ↓
Tools
 ├── Database
 ├── Files
 └── Web API
```

Then build a security layer that detects and blocks unsafe tool use.

---

# 📚 GitHub / Reference Library

Don't try to read these repositories from top to bottom.

Use them as references when you reach the relevant topic.

## Roadmaps

- [Red Team Roadmap](https://github.com/keraattin/Red-Team-Roadmap)
- [Red Team Arsenal](https://github.com/vamanparmar/red-team-arsenal)

## Web Security

- [Web Penetration Testing Roadmap](https://github.com/PracticeDevZone/Web_Penetration_Testing_Roadmap)
- [HackTricks](https://github.com/HackTricks-wiki/hacktricks)
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)

## Active Directory

- [ActiveDirectory-Pentest-Resources](https://github.com/daniellowrie/ActiveDirectory-Pentest-Resources)
- [Active Directory Pentesting](https://github.com/vimalraj-sec/active-directory-pentesting)
- [GOAD](https://github.com/Orange-Cyberdefense/GOAD)

## Security Wordlists / Enumeration

- [SecLists](https://github.com/danielmiessler/SecLists)

## Privilege Escalation

- [PEASS-ng](https://github.com/peass-ng/PEASS-ng)
- [GTFOBins](https://github.com/GTFOBins/GTFOBins)
- [LOLBAS](https://github.com/LOLBAS-Project/LOLBAS)

## Windows / AD Tooling

- [Impacket](https://github.com/fortra/impacket)

---

# 🧪 Project Portfolio

By the end of the roadmap, aim for **5–7 serious projects**, not dozens of tiny scripts.

| #  | Project                    | Skills                            |
| -- | -------------------------- | --------------------------------- |
| 1  | Network Traffic Analyzer   | Python, networking, Wireshark     |
| 2  | Mini Pentest Lab           | Nmap, enumeration, reporting      |
| 3  | Vulnerable Web App         | Next.js, Node, APIs, web security |
| 4  | Linux PrivEsc Lab          | Linux, permissions, security      |
| 5  | AD Attack & Detection Lab  | Windows, AD, Kerberos             |
| 6  | Attack Detection Platform  | Sysmon, SIEM, Python              |
| 7  | Automated Recon Tool       | Python, networking, automation    |
| 8  | Vulnerability Scanner      | HTTP, validation, reporting       |
| 9  | Mini CTF Platform          | Full-stack + security             |
| 10 | Telecom Security Simulator | SS7/SIGTRAN/MAP concepts          |

You don't need to build all ten. **Five excellent projects beat ten unfinished ones.**

---

# 🎯 Recommended Course + Project Order

## Stage 1 — Foundation

**Linux → Networking → Cybersecurity Fundamentals**

Build:

> Network Traffic Analyzer

---

## Stage 2 — Hacking

**Hacking Ki Series → Pentesting Fundamentals**

Build:

> Mini Pentest Lab

---

## Stage 3 — Web

**Web Security → Burp Suite → OWASP**

Build:

> Vulnerable Web Application

---

## Stage 4 — System Security

**Linux PrivEsc → Windows Fundamentals**

Build:

> Privilege Escalation Lab

---

## Stage 5 — Enterprise Red Team

**Active Directory → Kerberos → Windows Security**

Build:

> AD Attack & Detection Lab

---

## Stage 6 — Red Team

**MITRE ATT&CK → Adversary Simulation → Detection**

Build:

> Attack Detection Platform

---

## Stage 7 — Security Engineering

Build:

> Automated Recon Tool

> Vulnerability Scanner

> Mini CTF Platform

---

## Stage 8 — Specialization

Choose one:

```text
Active Directory / Red Team
        OR
Web Security
        OR
Cloud Security
        OR
Telecom Security
        OR
Exploit Development
        OR
AI Security
```

---

# 🧠 How to Study

Don't follow:

```text
Course
 ↓
Course
 ↓
Course
 ↓
Certificate
```

Follow:

```text
Learn a concept
      ↓
Build a lab
      ↓
Break your lab
      ↓
Understand why it worked
      ↓
Inspect logs / traffic
      ↓
Build detection
      ↓
Build your own tool
      ↓
Document everything
```

---

# 🏁 End Goal

You should eventually be able to look at a system and reason about:

```text
What is exposed?
       ↓
What can be abused?
       ↓
Why does it work?
       ↓
What would the attack look like?
       ↓
What evidence would it leave?
       ↓
How could it be detected?
       ↓
How should it be fixed?
       ↓
Can I automate the analysis?
```

That's the mindset you're aiming for.

## 🔴 Final Principle

**Don't become a person who knows 500 hacking commands.**

Become someone who can:

**Understand systems → find weaknesses → safely simulate attacks → analyze the results → build security tooling → explain and fix the problem.**
