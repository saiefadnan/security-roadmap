#!/usr/bin/env python3
"""
analyzer.py - Network Traffic Analyzer
Author: You!

Goal:
1. Capture packets live with sniff() OR read from 'sample.pcap' with rdpcap().
2. Extract:
   - Source IP & Destination IP
   - Protocol (TCP / UDP / ARP / ICMP)
   - Destination Ports
   - DNS Queries
   - HTTP Requests
3. Print out a summary of the captured traffic.
"""
from collections import Counter
from scapy.all import rdpcap, sniff, IP, TCP, UDP, ARP, DNSQR, Raw


class PacketAnalyzer:
    def __init__(self):
        self.total_packets=0
        self.protocols=Counter()
        self.src_ips=Counter()
        self.dst_ips=Counter()
        self.src_ports=Counter()
        self.dst_ports=Counter()
        self.dns_queries=[]
        self.http_requests=[]

    def analyze(self,packet):
        self.total_packets += 1
        # layer 2
        if packet.haslayer(ARP):
            self.protocols["ARP"]+=1
            self.src_ips[packet[ARP].psrc]+=1
            self.dst_ips[packet[ARP].pdst]+=1
            return
        
        # layer 4
        if packet.haslayer(IP):
            self.src_ips[packet[IP].src]+=1
            self.dst_ips[packet[IP].dst]+=1

            if packet.haslayer(TCP):
                self.protocols["TCP"]+=1
                self.src_ports[packet[TCP].sport]+=1
                self.dst_ports[packet[TCP].dport]+=1

                if packet.haslayer(Raw):
                    payload = packet[Raw].load.decode(errors="ignore")
                    if payload.startswith(("GET", "POST", "DELETE", "PUT", "PATCH")):
                        http_request = {
                            "method": payload.split()[0],
                            "path": payload.split()[1],
                            "src_ip": packet[IP].src,
                            "src_port": packet[TCP].sport,
                            "dst_ip": packet[IP].dst,
                            "dst_port": packet[TCP].dport,
                        }
                        self.http_requests.append(http_request)
                
                
            elif packet.haslayer(UDP):
                self.protocols["UDP"]+=1
                self.src_ports[packet[UDP].sport]+=1
                self.dst_ports[packet[UDP].dport]+=1

                if packet.haslayer(DNSQR):
                    qname = packet[DNSQR].qname.decode('utf-8')
                    qtype = packet[DNSQR].sprintf("%qtype%")
                    obj = {
                        "query": qname,
                        "type": qtype,
                        "src_ip": packet[IP].src,
                        "dst_ip": packet[IP].dst,
                        "sport": packet[UDP].sport,
                        "dport": packet[UDP].dport,
                    }
                    self.dns_queries.append(obj)



    def print_report(self):
        print("\n" + "=" * 65)
        print("          🌐 NETWORK TRAFFIC ANALYZER DASHBOARD")
        print("=" * 65)
        print(f"[*] Total Packets Analyzed: {self.total_packets}\n")

        # 1. Protocols with Visual Progress Bars
        print("┌── [ PROTOCOLS ] " + "─" * 45)
        for proto, count in self.protocols.most_common():
            pct = (count / self.total_packets) * 100 if self.total_packets else 0
            bar = "█" * int(pct // 10) + "░" * (10 - int(pct // 10))
            print(f"│ {proto:<10} : {count:>4} pkts ({pct:>5.1f}%)  [{bar}]")
        print("└" + "─" * 63 + "\n")

        # 2. Top Talker IPs (Source)
        print("┌── [ TOP TALKERS (SOURCE IPs) ] " + "─" * 32)
        for ip, count in self.src_ips.most_common(5):
            print(f"│ {ip:<25} -> {count:>4} packets")
        print("└" + "─" * 63 + "\n")

        # 3. Top Active Destination Ports & Service Names
        print("┌── [ TOP DESTINATION PORTS ] " + "─" * 35)
        known_services = {80: "HTTP", 443: "HTTPS", 53: "DNS", 22: "SSH", 123: "NTP"}
        for port, count in self.dst_ports.most_common(5):
            service = known_services.get(port, "Unknown")
            print(f"│ Port {port:<6} ({service:<7}) : {count:>4} packets")
        print("└" + "─" * 63 + "\n")

        # 4. Intercepted DNS Queries
        print("┌── [ DNS QUERIES INTERCEPTED ] " + "─" * 33)
        if self.dns_queries:
            for item in self.dns_queries:
                print(f"│ {item['src_ip']} queried '{item['query']}' (Type {item['type']})")
        else:
            print("│ No DNS queries captured.")
        print("└" + "─" * 63 + "\n")

        # 5. Intercepted HTTP Requests
        print("┌── [ HTTP REQUESTS INTERCEPTED ] " + "─" * 31)
        if self.http_requests:
            for item in self.http_requests:
                print(f"│ {item['src_ip']} -> {item['method']} {item['path']}")
        else:
            print("│ No unencrypted HTTP requests captured.")
        print("└" + "─" * 63)
        print("=" * 65 + "\n")



def main():
    pa = PacketAnalyzer()
    packets = sniff(count=10)
    for packet in packets:
        pa.analyze(packet)

    pa.print_report()

if __name__ == "__main__":
    main()
# --- START CODING HERE ---

