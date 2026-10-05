# 🟢 Phase 1 — Linux Fundamentals

## Overview
Phase 1 prepares you to work comfortably and securely in Linux from the command line, understanding:
1. **The Filesystem Hierarchy:** Where configuration files, logs, processes, and user data are stored.
2. **Users, Groups & Permissions:** Who can read, write, or execute files (`chmod`, `chown`, SUID).
3. **Processes & Services:** How programs run in the background, listening ports, and `/proc`.
4. **Networking & Sockets:** How machines communicate, network interfaces, and socket states (`ss -tulnp`).
5. **SSH & Environment Hardening:** Securing remote administration and avoiding PATH injection flaws.
6. **Shell Scripting & Log Analysis:** Automating tasks, parsing logs, and building security reconnaissance tools.

---

## 🗺️ Modules & Completed Notes

### 📂 [01-filesystem-and-permissions](file:///e:/my_projects/hack/phase-01-linux-fundamentals/01-filesystem-and-permissions)
* [01-filesystem-basics.md](file:///e:/my_projects/hack/phase-01-linux-fundamentals/01-filesystem-and-permissions/01-filesystem-basics.md): Linux directory tree (`/etc`, `/var`, `/home`, `/root`, `/tmp`, `/proc`).
* [02-users-and-passwd.md](file:///e:/my_projects/hack/phase-01-linux-fundamentals/01-filesystem-and-permissions/02-users-and-passwd.md): `/etc/passwd`, `/etc/shadow`, UID/GID, sudo privileges.
* [03-permissions-and-chmod.md](file:///e:/my_projects/hack/phase-01-linux-fundamentals/01-filesystem-and-permissions/03-permissions-and-chmod.md): Read/Write/Execute bits, octal representation (`755`, `644`), SUID/SGID bits.

### ⚙️ [02-processes-and-networking](file:///e:/my_projects/hack/phase-01-linux-fundamentals/02-processes-and-networking)
* [01-processes-and-services.md](file:///e:/my_projects/hack/phase-01-linux-fundamentals/02-processes-and-networking/01-processes-and-services.md): PIDs, `ps aux`, `top`, signals (`kill -9`), and `systemctl`.
* [02-packages-and-networking.md](file:///e:/my_projects/hack/phase-01-linux-fundamentals/02-processes-and-networking/02-packages-and-networking.md): Package management (`apt`), listening ports (`ss -tulpn`), interface inspection (`ip a`).
* [03-ssh-and-environment.md](file:///e:/my_projects/hack/phase-01-linux-fundamentals/02-processes-and-networking/03-ssh-and-environment.md): Key authentication, `/etc/ssh/sshd_config` hardening, `$PATH` hijacking vectors.
* [04-bash-scripting-fundamentals.md](file:///e:/my_projects/hack/phase-01-linux-fundamentals/02-processes-and-networking/04-bash-scripting-fundamentals.md): Robust scripting (`set -euo pipefail`), variables, conditionals, loops, streams.

---

## 🧪 Hands-On Mini Projects

### 🛡️ [Mini Project #1: Linux Auth Log Analyzer](file:///e:/my_projects/hack/phase-01-linux-fundamentals/03-mini-projects/log-analyzer/README.md)
* **Goal:** Parse `/var/log/auth.log` to detect SSH brute-force attacks, targeted usernames, and unauthorized sudo attempts.
* **Implementations:**
  - Python security parser: [`analyzer.py`](file:///e:/my_projects/hack/phase-01-linux-fundamentals/03-mini-projects/log-analyzer/analyzer.py)
  - One-line command line Bash pipeline: [`analyzer.sh`](file:///e:/my_projects/hack/phase-01-linux-fundamentals/03-mini-projects/log-analyzer/analyzer.sh)

### 🌐 [Mini Project #2: Network Information & Recon Tool](file:///e:/my_projects/hack/phase-01-linux-fundamentals/03-mini-projects/net-info-tool/README.md)
* **Goal:** Enumerate host network interfaces, IPv4/IPv6 CIDR, default gateway, DNS resolvers, listening ports, and security indicators (promiscuous mode, IP forwarding, local-only listeners).
* **Implementations:**
  - Pure Bash reconnaissance script: [`netinfo.sh`](file:///e:/my_projects/hack/phase-01-linux-fundamentals/03-mini-projects/net-info-tool/netinfo.sh)
  - Cross-platform Python parser with JSON output: [`netinfo.py`](file:///e:/my_projects/hack/phase-01-linux-fundamentals/03-mini-projects/net-info-tool/netinfo.py)

---

## 🖼️ Educational Visual Cards
All visual diagrams for Phase 1 are organized in [`images/`](file:///e:/my_projects/hack/phase-01-linux-fundamentals/images):
- `01-linux-permissions-cards.jpg`: 3-card breakdown of Permission Triad, Octal Math (`r=4, w=2, x=1`), and SUID (`4755`) Privilege Hazard.
- `02-linux-recon-flow.jpg`: 3-card flow of Interfaces (`lo` vs `eth0`), Socket Exposure (`127.0.0.1` vs `0.0.0.0`), and Kernel IP Forwarding.

