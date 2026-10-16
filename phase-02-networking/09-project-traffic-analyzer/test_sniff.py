#!/usr/bin/env python3
"""
Step 2: Minimal Scapy Packet Sniffer
Tests basic packet capture functionality.
"""
from scapy.all import sniff, IP, TCP, UDP, DNS, DNSQR, Raw, ARP

def packet_callback(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        proto = "OTHER"

        if packet.haslayer(TCP):
            proto = "TCP"
            sprt = packet[TCP].sport
            dport = packet[TCP].dport
            print(f"[*] {proto:5} | {src}:{sprt} -> {dst}:{dport}")
        
            if packet.haslayer(Raw):
                payload = packet[Raw].load.decode(errors='ignore')
                if payload.startswith(("GET", "POST", "HEAD")):
                    print(f"    └── [HTTP REQUEST] {payload.splitlines()[0]}")

        elif packet.haslayer(UDP):
            proto = "UDP"
            sprt = packet[UDP].sport
            dport = packet[UDP].dport
            print(f"[*] {proto:5} | {src}:{sprt} -> {dst}:{dport}")
            
            if packet.haslayer(DNSQR):
                qname = packet[DNSQR].qname.decode(errors='ignore')
                print(f"    └── [DNS QUERY] Looking up: {qname}")

    elif packet.haslayer(ARP):
        print(f"[*] ARP   | {packet[ARP].psrc} -> {packet[ARP].pdst} (who has query)")


def main():
    print("[*] Sniffing (filtered for TCP, DNS, or ARP - run curl or dig)...")
    # Using BPF filter to ignore background NTP chatter
    sniff(filter="tcp or port 53 or arp", count=10, prn=packet_callback)
    print("[*] Successfully captured 10 packets! Exiting.")

if __name__ == "__main__":
    main()
