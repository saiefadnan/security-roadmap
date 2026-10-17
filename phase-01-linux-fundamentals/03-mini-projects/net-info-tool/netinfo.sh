#!/usr/bin/env bash

echo "========================================"
echo "  🌐 Network Information Recon Tool"
echo "  Host: $(hostname)"
echo "========================================"

echo ""
echo "[+] 1. Network Interfaces & IP Addresses"
ip -brief address show

echo ""
echo "[+] 2. Default Gateway & Routes:"
ip route show

echo ""
echo "[+] 3. DNS Configuration (/etc/resolv.conf):"
grep "nameserver" /etc/resolv.conf

echo ""
echo "[+] 4. Listening Sockets (Open ports):"
ss -tulnp

echo ""
echo "[+] 5. Active Established Connections:"
ss -tun state established 

echo ""
echo "[+] 6. Security & Routing Indicators:"
echo -n "  IP Forwarding (1=Router, 0=Disabled): "
cat /proc/sys/net/ipv4/ip_forward


# Turn it ON=1 else OFF=0:
sudo sysctl -w net.ipv4.ip_forward=0

echo ""
echo "[+] 7. Public Internet IP:"
curl -s --max-time 3 ifconfig.me || echo "  (Offline or no internet route)"
