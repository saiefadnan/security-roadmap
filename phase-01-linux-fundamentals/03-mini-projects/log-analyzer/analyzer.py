#!/usr/bin/env python3
"""
Linux Auth Log Analyzer
Author: Security Engineering Lab
Purpose: Parse /var/log/auth.log to identify SSH brute-force attempts,
         suspicious sudo commands, and unauthorized user access.
"""

import re
import sys
from collections import Counter
from pathlib import Path

# ANSI Color codes for clean terminal output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Regular expressions for SSH & sudo events
SSH_FAILED_REGEX = re.compile(
    r"sshd\[\d+\]: Failed password for (?:invalid user )?(?P<user>\S+) from (?P<ip>\S+)"
)
SSH_ACCEPTED_REGEX = re.compile(
    r"sshd\[\d+\]: Accepted password for (?P<user>\S+) from (?P<ip>\S+)"
)
SUDO_FAIL_REGEX = re.compile(
    r"sudo:\s+(?P<user>\S+)\s+:\s+(?P<reason>.*?);\s+.*COMMAND=(?P<cmd>.*)"
)

BRUTE_FORCE_THRESHOLD = 3  # Flag IP if failed attempts >= threshold


def parse_log(file_path: Path):
    failed_ips = Counter()
    failed_users = Counter()
    accepted_logins = []
    sudo_alerts = []
    total_lines = 0

    if not file_path.exists():
        print(f"{RED}[!] Error: Log file not found at: {file_path}{RESET}")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            total_lines += 1

            # 1. Check for Failed SSH logins
            fail_match = SSH_FAILED_REGEX.search(line)
            if fail_match:
                ip = fail_match.group("ip")
                user = fail_match.group("user")
                failed_ips[ip] += 1
                failed_users[user] += 1
                continue

            # 2. Check for Accepted SSH logins
            ok_match = SSH_ACCEPTED_REGEX.search(line)
            if ok_match:
                accepted_logins.append(
                    {"user": ok_match.group("user"), "ip": ok_match.group("ip")}
                )
                continue

            # 3. Check for Suspicious Sudo events
            sudo_match = SUDO_FAIL_REGEX.search(line)
            if sudo_match:
                reason = sudo_match.group("reason").strip()
                if "incorrect password" in reason or "NOT in sudoers" in reason:
                    sudo_alerts.append(
                        {
                            "user": sudo_match.group("user"),
                            "reason": reason,
                            "command": sudo_match.group("cmd").strip(),
                        }
                    )

    return {
        "total_lines": total_lines,
        "failed_ips": failed_ips,
        "failed_users": failed_users,
        "accepted_logins": accepted_logins,
        "sudo_alerts": sudo_alerts,
    }


def print_report(results: dict, log_path: Path):
    print(f"\n{BOLD}{CYAN}==================================================={RESET}")
    print(f"{BOLD}{CYAN}      🛡️  LINUX AUTHENTICATION SECURITY REPORT       {RESET}")
    print(f"{BOLD}{CYAN}==================================================={RESET}")
    print(f"Target Log File : {log_path}")
    print(f"Total Lines Read: {results['total_lines']}\n")

    # 1. Accepted Logins
    print(f"{BOLD}[+] Successful Logins ({len(results['accepted_logins'])}){RESET}")
    if results["accepted_logins"]:
        for item in results["accepted_logins"]:
            print(f"    {GREEN}✔{RESET} User: {BOLD}{item['user']:<10}{RESET} from IP: {item['ip']}")
    else:
        print("    None recorded.")

    # 2. SSH Brute Force Detection
    print(f"\n{BOLD}[!] SSH Failed Login Attempts by IP{RESET}")
    brute_force_detected = False
    for ip, count in results["failed_ips"].most_common():
        if count >= BRUTE_FORCE_THRESHOLD:
            brute_force_detected = True
            print(f"    {RED}🔥 [HIGH RISK]{RESET} IP: {BOLD}{ip:<15}{RESET} -> {RED}{count} failed attempts{RESET} (Brute-force alert!)")
        else:
            print(f"    {YELLOW}⚠ [WARNING]{RESET}   IP: {BOLD}{ip:<15}{RESET} -> {count} failed attempts")

    if not results["failed_ips"]:
        print("    No failed login attempts found.")

    # 3. Top Targeted Usernames
    print(f"\n{BOLD}[!] Top Targeted Usernames{RESET}")
    for user, count in results["failed_users"].most_common(5):
        print(f"    - {BOLD}{user:<12}{RESET}: {count} attempt(s)")

    # 4. Sudo Security Alerts
    print(f"\n{BOLD}[!] Suspicious Sudo Activity ({len(results['sudo_alerts'])}){RESET}")
    if results["sudo_alerts"]:
        for alert in results["sudo_alerts"]:
            print(f"    {RED}🚨 User '{alert['user']}'{RESET} failed sudo:")
            print(f"       Reason : {YELLOW}{alert['reason']}{RESET}")
            print(f"       Command: {BOLD}{alert['command']}{RESET}")
    else:
        print("    No suspicious sudo violations.")

    print(f"\n{BOLD}{CYAN}==================================================={RESET}")
    print(f"{BOLD}Summary & Recommendations:{RESET}")
    if brute_force_detected:
        print(f"  {RED}• Recommendation:{RESET} Block high-risk IPs using `iptables` or install `fail2ban`.")
    if results["sudo_alerts"]:
        print(f"  {YELLOW}• Recommendation:{RESET} Audit sudo permissions and investigate unauthorized command attempts.")
    if not brute_force_detected and not results["sudo_alerts"]:
        print(f"  {GREEN}• System appears calm:{RESET} No high-risk anomalies detected.")
    print(f"{BOLD}{CYAN}==================================================={RESET}\n")


def main():
    target_file = (
        Path(sys.argv[1])
        if len(sys.argv) > 1
        else Path(__file__).parent / "sample_auth.log"
    )
    results = parse_log(target_file)
    print_report(results, target_file)


if __name__ == "__main__":
    main()
