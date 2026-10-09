# 🔐 Step 4: Authentication, Authorization & Cryptography

> **Phase 3: Cybersecurity Fundamentals**  
> *"Authentication proves who you are; Authorization decides what you can do. Encryption protects secrets in transit; Hashing proves secrets without revealing them."*

---

## 1. Authentication (AuthN) vs. Authorization (AuthZ)

| Feature | Authentication (AuthN) | Authorization (AuthZ) |
| :--- | :--- | :--- |
| **Core Question** | *"Who are you?"* | *"What are you allowed to do?"* |
| **Focus** | Verifying identity. | Enforcing permissions & access boundaries. |
| **Mechanisms** | Passwords, MFA tokens, FaceID, SSH public keys, Biometrics. | Linux file modes (`rwxr-xr-x`, SUID), RBAC, sudoers, ACLs. |
| **Attacks** | Credential stuffing, password spraying, phishing, brute-force. | Privilege escalation, IDOR, parameter tampering. |

---

## 2. Encryption vs. Hashing (Two-Way vs. One-Way)

```text
ENCRYPTION (Two-Way with Key):
  Plaintext ──────► [ Encrypt with Key ] ──────► Ciphertext
  Ciphertext ─────► [ Decrypt with Key ] ──────► Plaintext

HASHING (One-Way Mathematical Digest):
  Plaintext ──────► [ SHA-256 / bcrypt ] ──────► Fixed-Length Hash
  Hash ───────────► [ CANNOT REVERSE ]   ──────► ❌ Impossible
```

| Property | Encryption | Hashing |
| :--- | :--- | :--- |
| **Reversibility** | **Two-way:** Can be decrypted with the mathematical key. | **One-way:** Mathematically irreversible. |
| **Output Length** | Varies depending on plaintext input size. | **Fixed length** (MD5: 32 hex chars, SHA-256: 64 hex chars). |
| **Primary Goal** | Confidentiality of data in transit (TLS) or at rest (BitLocker). | Integrity verification and secure password storage. |
| **Algorithms** | AES-256, ChaCha20, RSA. | SHA-256, SHA-3, bcrypt, Argon2 (Legacy: MD5, SHA-1). |

---

## 3. Password Storage, Salting & Hash Cracking

### Why We Hash Passwords:
If a database is breached, the attacker only gets hashes. They cannot immediately read plaintext passwords.

### How Hackers Attack Hashes (Dictionary & Rainbow Tables):
Because hashing is deterministic (`"password"` always hashes to `5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8`), attackers compute hashes of millions of common passwords in advance (**Rainbow Tables**).

### The Defense: Salting
Systems prepend random bytes to the password before hashing:
$$\text{Stored Hash} = \text{Hash}(\text{Password} + \mathbf{Random\ Salt})$$
- Even if two users choose the exact same password (`Password123`), their random salts produce completely different hashes.
- Renders pre-computed rainbow tables completely useless!
- Modern password hashing algorithms like **bcrypt** and **Argon2** include built-in salting and adjustable computation costs (work factors) to slow down GPU brute-forcing.
