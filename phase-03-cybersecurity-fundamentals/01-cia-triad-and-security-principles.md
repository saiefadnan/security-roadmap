# 🛡️ Step 1: The CIA Triad & Core Security Principles

> **Phase 3: Cybersecurity Fundamentals**  
> *"Every defense is built to protect these three pillars; every exploit is written to shatter one of them."*

---

## 1. The Core Triad

```text
                     ┌──────────────────┐
                     │    CIA TRIAD     │
                     └────────┬─────────┘
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
 [ Confidentiality ]     [ Integrity ]       [ Availability ]
  "Keep secrets         "Prevent tampering    "Keep systems up
   secret."              or modification."     and running."
```

| Pillar | Definition | Defensive Controls | Offensive Attack Vectors |
| :--- | :--- | :--- | :--- |
| **Confidentiality** | Ensuring sensitive data is only accessible to authorized entities. | Encryption (AES, TLS), Access Control Lists (ACLs), MFA, Data Loss Prevention (DLP). | Packet sniffing, SQL injection dumping DBs, credential theft, eavesdropping. |
| **Integrity** | Guaranteeing data is accurate, complete, and protected from unauthorized modification. | Cryptographic Hashing (SHA-256), Digital Signatures, HMACs, Version control. | Parameter tampering, DNS cache poisoning, Man-in-the-Middle payload injection. |
| **Availability** | Ensuring systems, networks, and applications are operational and accessible to authorized users when needed. | Redundancy, Load Balancers, DDoS mitigation, Backups, High Availability (HA) clustering. | Volumetric DDoS, Ransomware disk encryption, SYN flood exhaustion, Resource exhaustion. |

---

## 2. Non-Repudiation & The Extended Security Model

Beyond the classic CIA triad, modern security architectures include:

1. **Authentication:** Proving **who** you are (Passwords, SSH keys, MFA tokens).
2. **Authorization:** Defining **what** you are allowed to do (RBAC permissions, SUID/sudo access).
3. **Non-Repudiation:** Mathematical proof that a specific user performed an action, preventing them from denying it later (Cryptographic digital signatures, tamper-evident audit logs).
4. **Accountability (Auditing):** Tracking actions to a specific identity through secure logging (`/var/log/auth.log`).
