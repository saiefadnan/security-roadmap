# 🛡️ Step 6: Defensive Controls — IDS, IPS & SIEM

> **Phase 3: Cybersecurity Fundamentals**  
> *"An IDS sounds the alarm, an IPS tackles the intruder, and a SIEM correlates footage from the entire building."*

---

## 1. The Classes of Security Controls

Organizations deploy three fundamental types of security controls:

```text
┌─────────────────────────┐       ┌─────────────────────────┐       ┌─────────────────────────┐
│       PREVENTIVE        │       │        DETECTIVE        │       │       CORRECTIVE        │
│    "Stop the attack"    │       │   "Spot the intruder"   │       │   "Recover & restore"   │
└─────────────────────────┘       └─────────────────────────┘       └─────────────────────────┘
```

1. **Preventive Controls:** Prevent security incidents from occurring (Firewalls, MFA, encryption, least privilege).
2. **Detective Controls:** Identify and alert on malicious activity while it is happening or after the fact (IDS, audit logs, file integrity monitoring, SIEM).
3. **Corrective Controls:** Mitigate damage and restore systems back to normal operations (Backups, incident response plans, automated isolation).

---

## 2. IDS vs. IPS (Intrusion Detection vs. Prevention)

| Feature | IDS (Intrusion Detection System) | IPS (Intrusion Prevention System) |
| :--- | :--- | :--- |
| **Network Position** | **Out-of-band / Passive** (Connected to a switch SPAN / mirror port). | **In-line** (Directly in the physical path of network traffic). |
| **Primary Action** | Detects and **ALERTS** the security team. | Detects and **DROPS / BLOCKS** the malicious packets in real time. |
| **Attack Impact** | The malicious packet **still reaches** the target server! | The attack packet is terminated on the wire (sends TCP `RST`). |
| **Operational Risk** | Zero risk of breaking legitimate business traffic. | False positives can accidentally block legitimate customers. |
| **Industry Tools** | Snort, Suricata, Zeek. | Snort (in-line mode), Palo Alto Networks, Cisco Firepower. |

---

## 3. SIEM (Security Information & Event Management)

In enterprise networks with thousands of servers, workstations, and network devices, security teams cannot look at individual logs. A **SIEM** acts as the central brain of the **SOC (Security Operations Center)**:

```text
[ Linux auth.log ] ────┐
[ Windows Events ] ────┼──► [ SIEM Central Ingestion & Parser ] ──► [ Correlation Engine ] ──► 🚨 SOC Alert!
[ Firewall Drops ] ────┤          (Splunk / Sentinel)                "Correlates brute-force +
[ IDS Alerts     ] ────┘                                              privilege escalation"
```

### Core Superpowers of a SIEM:
1. **Centralized Log Aggregation:** Ingests terabytes of logs daily from every endpoint, cloud provider, and firewall.
2. **Event Correlation:** Connects separate breadcrumbs across multiple systems:
   - *Example:* A failed SSH login in Linux + a new scheduled task created in Windows + unusual DNS traffic = **High Severity Compromise Alert**.
3. **Compliance & Forensics:** Stores tamper-proof historical audit logs for regulatory compliance (PCI-DSS, HIPAA, ISO 27001).
