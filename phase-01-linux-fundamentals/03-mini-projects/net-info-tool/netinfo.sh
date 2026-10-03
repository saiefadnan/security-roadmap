#!/usr/bin/env bash
# ==============================================================================
# 🌐 Linux Network Information & Situational Awareness Recon Tool
# Purpose: Gathers network interfaces, IPs, default routes, DNS servers,
#          listening sockets, and offensive/defensive indicators.
# ==============================================================================

# ANSI Color Codes for readability
RED="\033[1;31m"
GREEN="\033[1;32m"
YELLOW="\033[1;33m"
BLUE="\033[1;34m"
CYAN="\033[1;36m"
BOLD="\033[1m"
RESET="\033[0m"

print_header() {
    echo -e "${CYAN}================================================================${RESET}"
    echo -e "${BOLD}${BLUE}  🌐 NETWORK INFORMATION & SITUATIONAL AWARENESS TOOL${RESET}"
    echo -e "${CYAN}================================================================${RESET}"
    echo -e "Hostname  : ${BOLD}$(hostname)${RESET}"
    echo -e "Kernel    : $(uname -r)"
    echo -e "Date/Time : $(date -u '+%Y-%m-%d %H:%M:%S UTC')"
    echo ""
}

# 1. Network Interfaces & IP Addresses
get_interfaces() {
    echo -e "${BOLD}${YELLOW}[+] 1. Network Interfaces & Addresses:${RESET}"
    echo -e "    ${BOLD}Command: ip -brief address show${RESET}"
    echo "----------------------------------------------------------------"
    if command -v ip &>/dev/null; then
        # -brief provides interface name, operational state, and IPv4/IPv6 CIDR addresses
        ip -brief address show | while read -r iface state addrs; do
            if [ "$state" = "UP" ]; then
                state_color="${GREEN}${state}${RESET}"
            else
                state_color="${RED}${state}${RESET}"
            fi
            printf "  %-12s [%b]  %s\n" "$iface" "$state_color" "$addrs"
        done
        echo ""
        echo -e "    ${BOLD}Hardware (MAC) Addresses (ip link show):${RESET}"
        ip -brief link show | while read -r iface state mac rest; do
            printf "  %-12s MAC: %-18s (flags: %s)\n" "$iface" "$mac" "$rest"
        done
    else
        # Fallback to ifconfig if ip is absent
        ifconfig -a 2>/dev/null || echo "    [!] Neither 'ip' nor 'ifconfig' command found."
    fi
    echo ""
}

# 2. Routing Table & Default Gateway
get_gateway() {
    echo -e "${BOLD}${YELLOW}[+] 2. Default Gateway & Routing Table:${RESET}"
    echo -e "    ${BOLD}Command: ip route show${RESET}"
    echo "----------------------------------------------------------------"
    if command -v ip &>/dev/null; then
        local def_route
        def_route=$(ip route show default 2>/dev/null)
        if [ -n "$def_route" ]; then
            echo -e "  ${GREEN}[✓] Default Gateway:${RESET} ${BOLD}${def_route}${RESET}"
        else
            echo -e "  ${RED}[!] No default gateway found (isolated network or host-only).${RESET}"
        fi
        echo ""
        echo -e "  Full Routing Table:"
        ip route show | sed 's/^/    /'
    else
        route -n 2>/dev/null || netstat -rn 2>/dev/null || echo "    [!] Routing tools not found."
    fi
    echo ""
}

# 3. DNS Resolvers
get_dns() {
    echo -e "${BOLD}${YELLOW}[+] 3. DNS Configuration:${RESET}"
    echo -e "    ${BOLD}Source: /etc/resolv.conf & systemd-resolved${RESET}"
    echo "----------------------------------------------------------------"
    if [ -f /etc/resolv.conf ]; then
        echo "  Nameservers in /etc/resolv.conf:"
        grep -E "^nameserver" /etc/resolv.conf | while read -r _ ns; do
            echo -e "    - ${BOLD}$ns${RESET}"
        done
        
        # Check for search domains
        local search_domains
        search_domains=$(grep -E "^(search|domain)" /etc/resolv.conf | awk '{print $2}')
        if [ -n "$search_domains" ]; then
            echo -e "  Search Domain(s): ${search_domains}"
        fi
    else
        echo -e "  ${RED}[!] /etc/resolv.conf not found.${RESET}"
    fi

    # Check if systemd-resolved is active
    if command -v resolvectl &>/dev/null; then
        echo ""
        echo "  Systemd-resolved DNS Status (per-interface):"
        resolvectl dns 2>/dev/null | sed 's/^/    /' || true
    fi
    echo ""
}

# 4. Open Ports / Listening Sockets
get_listeners() {
    echo -e "${BOLD}${YELLOW}[+] 4. Listening Sockets (Open Ports):${RESET}"
    echo -e "    ${BOLD}Command: ss -tulnp (or netstat -tulnp)${RESET}"
    echo "----------------------------------------------------------------"
    if command -v ss &>/dev/null; then
        echo -e "  ${BOLD}Proto  State       Local Address:Port          Process / PID${RESET}"
        # Filter for LISTEN (TCP) and UNCONN (UDP listeners)
        ss -tulnp 2>/dev/null | awk 'NR>1 {printf "  %-5s  %-10s  %-26s  %s\n", $1, $2, $5, $7}'
    elif command -v netstat &>/dev/null; then
        netstat -tulnp 2>/dev/null | sed 's/^/  /'
    else
        echo "  [!] Neither 'ss' nor 'netstat' available."
    fi
    echo ""
}

# 5. Active Established Connections
get_established() {
    echo -e "${BOLD}${YELLOW}[+] 5. Active Network Connections (Outbound / Inbound):${RESET}"
    echo -e "    ${BOLD}Command: ss -tun state established${RESET}"
    echo "----------------------------------------------------------------"
    if command -v ss &>/dev/null; then
        local conns
        conns=$(ss -tun state established 2>/dev/null | awk 'NR>1 {printf "  %-5s  Local: %-22s <---> Remote: %-22s\n", $1, $4, $5}')
        if [ -n "$conns" ]; then
            echo "$conns"
        else
            echo "  (No active ESTABLISHED TCP/UDP connections detected)"
        fi
    fi
    echo ""
}

# 6. Offensive & Defensive Security Indicators
get_security_checks() {
    echo -e "${BOLD}${YELLOW}[+] 6. Security & Pivoting Indicators:${RESET}"
    echo "----------------------------------------------------------------"
    
    # Check IP forwarding (Can this machine route packets between networks / pivot?)
    if [ -f /proc/sys/net/ipv4/ip_forward ]; then
        local ip_fwd
        ip_fwd=$(cat /proc/sys/net/ipv4/ip_forward)
        if [ "$ip_fwd" -eq 1 ]; then
            echo -e "  ${RED}[!] IP Forwarding is ENABLED${RESET} (Host can act as a router / pivot point)"
        else
            echo -e "  ${GREEN}[✓] IP Forwarding is Disabled${RESET}"
        fi
    fi

    # Check promiscuous mode on interfaces (Sniffing indicator)
    if command -v ip &>/dev/null; then
        local promisc
        promisc=$(ip link show | grep -i "PROMISC")
        if [ -n "$promisc" ]; then
            echo -e "  ${RED}[!] Promiscuous Mode Detected on:${RESET}"
            echo "$promisc" | sed 's/^/      /'
        else
            echo -e "  ${GREEN}[✓] No interfaces currently in promiscuous mode${RESET}"
        fi
    fi

    # Check for localhost-only services (Potential privilege escalation / SSRF targets)
    if command -v ss &>/dev/null; then
        local local_only
        local_only=$(ss -tlnp 2>/dev/null | grep -E "127\.0\.0\.1|::1" | awk '{print $4, $6}')
        if [ -n "$local_only" ]; then
            echo -e "  ${BLUE}[i] Localhost-only listeners (potential internal services):${RESET}"
            echo "$local_only" | while read -r addr proc; do
                echo -e "      - ${BOLD}$addr${RESET} ($proc)"
            done
        fi
    fi
    echo ""
}

# Main Execution Flow
print_header
get_interfaces
get_gateway
get_dns
get_listeners
get_established
get_security_checks

echo -e "${CYAN}================================================================${RESET}"
echo -e "${GREEN}[✓] Network reconnaissance scan complete.${RESET}"
echo -e "${CYAN}================================================================${RESET}"
