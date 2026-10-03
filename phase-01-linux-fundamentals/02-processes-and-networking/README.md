# ⚙️ Step 2: Processes, Ports & Networking

This module covers core administration, inspection, and automation skills required for Linux security, triage, and red teaming.

---

## 📚 Guides & Notes in this Section

1. **[01-processes-and-services.md](file:///e:/my_projects/hack/phase-01-linux-fundamentals/02-processes-and-networking/01-processes-and-services.md)**
   - Process hierarchy (`PID 1 / systemd`, parent/child PIDs).
   - Inspecting running programs (`ps aux`, `pstree`, `top`/`htop`).
   - Process control & signals (`kill -9`, `kill -15`, `killall`).
   - Managing daemons & services via `systemctl` (`start`, `stop`, `status`, `enable`).

2. **[02-packages-and-networking.md](file:///e:/my_projects/hack/phase-01-linux-fundamentals/02-processes-and-networking/02-packages-and-networking.md)**
   - Debian/Ubuntu package management (`apt update`, `apt install`).
   - Inspecting network interfaces (`ip addr`, `ip link`).
   - Inspecting listening ports and sockets (`ss -tulnp`).
   - Transferring files and banners (`curl`, `wget`, `nc`).

3. **[03-ssh-and-environment.md](file:///e:/my_projects/hack/phase-01-linux-fundamentals/02-processes-and-networking/03-ssh-and-environment.md)**
   - SSH asymmetric key authentication & strict permission modes (`chmod 600/700`).
   - SSH daemon hardening (`/etc/ssh/sshd_config`).
   - Environment variables (`export`, `/proc/$PID/environ`).
   - Security flaws: Secret leakage and PATH hijacking privilege escalation.

4. **[04-bash-scripting-fundamentals.md](file:///e:/my_projects/hack/phase-01-linux-fundamentals/02-processes-and-networking/04-bash-scripting-fundamentals.md)**
   - Anatomy of a robust script (`set -euo pipefail`).
   - Variables, positional parameters, and conditionals.
   - Loops, streams, and pipelines (`|`, `2>&1`, `/dev/null`).
   - Exit codes and error handling for security automation.

---

## 🚀 Practical Application
The concepts learned here directly feed into:
- **[Mini Project #1: Log Analyzer](file:///e:/my_projects/hack/phase-01-linux-fundamentals/03-mini-projects/log-analyzer/README.md)** (Detecting unauthorized processes and failed authentication).
- **[Mini Project #2: Network Information Tool](file:///e:/my_projects/hack/phase-01-linux-fundamentals/03-mini-projects/net-info-tool/README.md)** (Automating the discovery of network interfaces, routes, DNS, and open ports).
