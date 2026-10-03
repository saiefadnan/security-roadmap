#!/usr/bin/env python3
"""
Network Information & Situational Awareness Recon Tool (Python Edition)
========================================================================
Collects:
- Active Network Interfaces, MAC addresses, IPv4/IPv6 addresses
- Default Gateway & Routing Information
- DNS Resolvers and Search Domains
- Active & Listening Sockets (Open Ports)
- Security Indicators (Promiscuous mode, IP forwarding, Local-only services)

Supports human-readable output and JSON serialization for programmatic analysis.
"""

import sys
import os
import re
import json
import socket
import subprocess
import argparse
from typing import Dict, Any, List

# Ensure UTF-8 output on Windows consoles if supported
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass


def run_cmd(cmd: List[str]) -> str:
    """Helper to run a shell command safely and return stripped stdout."""
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        return res.stdout.strip()
    except Exception:
        return ""


def get_interfaces() -> List[Dict[str, Any]]:
    """Enumerate network interfaces, status, MAC addresses, and IPs."""
    interfaces = []
    
    # Try ip -json address show (modern Linux)
    ip_json = run_cmd(["ip", "-json", "address", "show"])
    if ip_json:
        try:
            data = json.loads(ip_json)
            for item in data:
                iface_name = item.get("ifname", "unknown")
                operstate = item.get("operstate", "UNKNOWN")
                mac = item.get("address", "")
                flags = item.get("flags", [])
                
                ipv4_list = []
                ipv6_list = []
                for addr_info in item.get("addr_info", []):
                    family = addr_info.get("family")
                    local_ip = addr_info.get("local")
                    prefixlen = addr_info.get("prefixlen")
                    cidr = f"{local_ip}/{prefixlen}" if local_ip and prefixlen else local_ip
                    if family == "inet":
                        ipv4_list.append(cidr)
                    elif family == "inet6":
                        ipv6_list.append(cidr)

                interfaces.append({
                    "name": iface_name,
                    "state": operstate,
                    "mac": mac,
                    "flags": flags,
                    "ipv4": ipv4_list,
                    "ipv6": ipv6_list
                })
            return interfaces
        except Exception:
            pass

    # Fallback parsing with 'ip -brief addr'
    brief_out = run_cmd(["ip", "-brief", "address", "show"])
    if brief_out:
        for line in brief_out.splitlines():
            parts = line.split()
            if len(parts) >= 2:
                name = parts[0]
                state = parts[1]
                addrs = parts[2:] if len(parts) > 2 else []
                ipv4 = [a for a in addrs if ":" not in a]
                ipv6 = [a for a in addrs if ":" in a]
                interfaces.append({
                    "name": name,
                    "state": state,
                    "mac": "",
                    "flags": [],
                    "ipv4": ipv4,
                    "ipv6": ipv6
                })
        return interfaces

    # Basic hostname fallback if ip command is not present (e.g. Windows native)
    try:
        host = socket.gethostname()
        ip_addr = socket.gethostbyname(host)
        interfaces.append({
            "name": "default",
            "state": "UP",
            "mac": "",
            "flags": [],
            "ipv4": [ip_addr],
            "ipv6": []
        })
    except Exception:
        pass

    return interfaces


def get_routing() -> Dict[str, Any]:
    """Retrieve default gateway and routing entries."""
    routing_info = {
        "default_gateway": None,
        "routes": []
    }
    
    route_out = run_cmd(["ip", "route", "show"])
    if route_out:
        for line in route_out.splitlines():
            routing_info["routes"].append(line)
            if line.startswith("default"):
                # Format: default via 192.168.1.1 dev eth0 proto dhcp metric 100
                m = re.search(r"default via (\S+)(?: dev (\S+))?", line)
                if m:
                    routing_info["default_gateway"] = {
                        "ip": m.group(1),
                        "interface": m.group(2) if m.group(2) else ""
                    }
    return routing_info


def get_dns() -> Dict[str, Any]:
    """Inspect nameservers from /etc/resolv.conf and systemd-resolved."""
    dns_info = {
        "nameservers": [],
        "search_domains": []
    }
    
    resolv_path = "/etc/resolv.conf"
    if os.path.exists(resolv_path):
        try:
            with open(resolv_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("nameserver"):
                        parts = line.split()
                        if len(parts) > 1:
                            dns_info["nameservers"].append(parts[1])
                    elif line.startswith("search") or line.startswith("domain"):
                        parts = line.split()
                        if len(parts) > 1:
                            dns_info["search_domains"].extend(parts[1:])
        except Exception:
            pass

    return dns_info


def get_listening_sockets() -> List[Dict[str, Any]]:
    """Find all listening TCP/UDP ports and associated processes."""
    listeners = []
    
    ss_out = run_cmd(["ss", "-tulnp"])
    if ss_out:
        lines = ss_out.splitlines()
        for line in lines[1:]:
            parts = line.split()
            if len(parts) >= 5:
                proto = parts[0]
                state = parts[1]
                local_addr = parts[4]
                process_info = parts[6] if len(parts) > 6 else ""
                listeners.append({
                    "protocol": proto,
                    "state": state,
                    "local_address": local_addr,
                    "process": process_info
                })
    return listeners


def get_security_indicators(interfaces: List[Dict[str, Any]], listeners: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Detect common security flags (IP forwarding, promiscuous sniffing, local-only listeners)."""
    indicators = {
        "ip_forwarding_enabled": False,
        "promiscuous_interfaces": [],
        "localhost_only_listeners": []
    }

    # IP forwarding check
    fwd_path = "/proc/sys/net/ipv4/ip_forward"
    if os.path.exists(fwd_path):
        try:
            with open(fwd_path, "r") as f:
                if f.read().strip() == "1":
                    indicators["ip_forwarding_enabled"] = True
        except Exception:
            pass

    # Promiscuous mode flag check
    for iface in interfaces:
        flags = iface.get("flags", [])
        if "PROMISC" in flags:
            indicators["promiscuous_interfaces"].append(iface["name"])

    # Local-only services (127.0.0.1 or ::1)
    for l in listeners:
        addr = l.get("local_address", "")
        if "127.0.0.1" in addr or "[::1]" in addr or addr.startswith("127."):
            indicators["localhost_only_listeners"].append(l)

    return indicators


def collect_all_data() -> Dict[str, Any]:
    """Aggregates all network telemetry into a structured dictionary."""
    hostname = socket.gethostname()
    ifaces = get_interfaces()
    routing = get_routing()
    dns = get_dns()
    listeners = get_listening_sockets()
    sec = get_security_indicators(ifaces, listeners)

    return {
        "hostname": hostname,
        "interfaces": ifaces,
        "routing": routing,
        "dns": dns,
        "listening_ports": listeners,
        "security_indicators": sec
    }


def print_human_report(data: Dict[str, Any]):
    """Pretty prints the reconnaissance report to the console."""
    print("=" * 66)
    print(f"  🌐 NETWORK RECONNAISSANCE & SITUATIONAL AWARENESS REPORT")
    print("=" * 66)
    print(f" Hostname : {data['hostname']}")
    print("-" * 66)

    # Interfaces
    print("\n[+] 1. Network Interfaces & Addresses:")
    for iface in data["interfaces"]:
        state_symbol = "🟢 UP" if iface["state"].upper() == "UP" else f"⚪ {iface['state']}"
        print(f"  * {iface['name']} [{state_symbol}]")
        if iface.get("mac"):
            print(f"    MAC Address : {iface['mac']}")
        if iface["ipv4"]:
            print(f"    IPv4 Address: {', '.join(iface['ipv4'])}")
        if iface["ipv6"]:
            print(f"    IPv6 Address: {', '.join(iface['ipv6'])}")

    # Gateway & Routes
    print("\n[+] 2. Gateway & Routes:")
    gw = data["routing"]["default_gateway"]
    if gw:
        print(f"  Default Gateway: {gw['ip']} (Interface: {gw.get('interface', 'n/a')})")
    else:
        print("  Default Gateway: Not configured / Isolated")
    
    if data["routing"]["routes"]:
        print("  Active Routes:")
        for r in data["routing"]["routes"]:
            print(f"    - {r}")

    # DNS
    print("\n[+] 3. DNS Configuration:")
    ns = data["dns"]["nameservers"]
    if ns:
        print(f"  Nameservers: {', '.join(ns)}")
    else:
        print("  Nameservers: None detected in /etc/resolv.conf")
    if data["dns"]["search_domains"]:
        print(f"  Search Domains: {', '.join(data['dns']['search_domains'])}")

    # Listening Sockets
    print("\n[+] 4. Open Ports (Listening Sockets):")
    listeners = data["listening_ports"]
    if listeners:
        print(f"  {'Proto':<6} {'State':<10} {'Local Address:Port':<28} {'Process'}")
        print("  " + "-" * 62)
        for l in listeners:
            print(f"  {l['protocol']:<6} {l['state']:<10} {l['local_address']:<28} {l['process']}")
    else:
        print("  No listening ports detected via ss (root permissions may be required for process names).")

    # Security & Pivot Indicators
    print("\n[+] 5. Security & Pivoting Indicators:")
    sec = data["security_indicators"]
    
    # IP Forwarding
    if sec["ip_forwarding_enabled"]:
        print("  [!] IP FORWARDING: ENABLED (Host can route packets between networks / pivot target)")
    else:
        print("  [✓] IP Forwarding: Disabled")

    # Promiscuous Interfaces
    if sec["promiscuous_interfaces"]:
        print(f"  [!] PROMISCUOUS INTERFACES: {', '.join(sec['promiscuous_interfaces'])} (Packet sniffing detected)")
    else:
        print("  [✓] Promiscuous Mode: None active")

    # Localhost only services
    local_listeners = sec["localhost_only_listeners"]
    if local_listeners:
        print(f"  [i] Localhost-Only Listeners ({len(local_listeners)} found - internal services):")
        for ll in local_listeners:
            print(f"      - {ll['local_address']} ({ll['process'] or 'PID hidden'})")
    else:
        print("  [✓] No local-only listeners detected.")

    print("\n" + "=" * 66)
    print("  [✓] Report complete.")
    print("=" * 66)


def main():
    parser = argparse.ArgumentParser(
        description="Linux Network Information & Situational Awareness Recon Tool"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results formatted as JSON"
    )
    args = parser.parse_args()

    data = collect_all_data()

    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print_human_report(data)


if __name__ == "__main__":
    main()
