# 🛡️ Mini Project #1: Linux Auth Log Analyzer

## Overview
This security tool parses Linux authentication logs (`/var/log/auth.log`) to uncover:
1. **SSH Brute-Force Attacks:** Identifies remote IP addresses repeatedly failing authentication.
2. **Targeted Usernames:** Pinpoints which usernames attackers are trying to crack (e.g. `root`, `admin`, `postgres`).
3. **Sudo Abuse & Violations:** Alerts on unauthorized sudo executions (e.g. users attempting to read `/etc/shadow` without permissions).
4. **Legitimate Logins:** Summarizes valid authorized sessions.

---

## Files in this Project
* **`sample_auth.log`**: A simulated attack log containing realistic SSH brute-force attempts from external IPs and suspicious sudo failures.
* **`analyzer.py`**: The core Python security parser. Uses regex and frequency counters with zero external dependencies.
* **`analyzer.sh`**: A quick, command-line Bash pipeline using `grep`, `awk`, `sort`, and `uniq` to extract offending IPs and targeted users in real-time.

---

## How to Run

### 1. Run Python Analyzer against the sample log:
```bash
cd /mnt/e/my_projects/hack/phase-01-linux-fundamentals/03-mini-projects/log-analyzer
python3 analyzer.py
```

### 2. Run Bash Analyzer against the sample log:
```bash
./analyzer.sh
```

### 2. Run against your real system log (requires root / sudo):
```bash
python3 analyzer.py /var/log/auth.log
```
