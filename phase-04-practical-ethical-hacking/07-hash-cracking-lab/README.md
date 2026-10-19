# 🧪 Practical Lab 07 — Password Cracking & Credential Security Workbench

> **Objective:** Hands-on experience with cryptographic hash algorithms (MD5, SHA-256, NTLM), dictionary attacks, rule-based mutations, and the mathematical defense of salt nonces.

---

## 🚀 How to Run the Hands-on Lab

You can run the interactive lab workbench directly in PowerShell or Linux terminal:

```bash
python phase-04-practical-ethical-hacking/07-hash-cracking-lab/hash_lab.py
```

---

## 🎯 Lab Modes & Capabilities

### Mode 1: Hash Generator
Input any plaintext password (e.g., `admin`, `secret2026!`) and observe the instantaneous generation of:
* **MD5:** 32 hex chars (legacy, fast).
* **SHA-256:** 64 hex chars (modern fast integrity hash).
* **NTLM:** 32 hex chars (Windows authentication hash).

### Mode 2: Dictionary Attack Engine
Simulates Hashcat's `-a 0` straight dictionary mode:
* Loads `phase-04-practical-ethical-hacking/wordlists/top-10000-passwords.txt`.
* Computes thousands of candidate hashes per second locally.
* Reports exact execution time, words searched, and effective hash rate ($\text{hashes/sec}$).

### Mode 3: Rule-Based Mutation Attack
Simulates Hashcat's rule-based engine (`-r`):
* What if the target used `dr@g0n2026!`? That word is **not** in any standard wordlist.
* You provide a suspected base word (e.g., `dragon`), and the engine applies leetspeak substitutions (`a` $\rightarrow$ `@`, `o` $\rightarrow$ `0`), capitalization rules, and common year/symbol suffixes to crack complex enterprise passwords.

### Mode 4: The Salt Defense Experiment
Demonstrates why unsalted NTLM hashes create severe enterprise risk:
* **Unsalted:** 3 different employee accounts with identical passwords yield **identical hashes**, allowing 1 crack to compromise 3 accounts.
* **Salted:** 3 employee accounts with unique salt nonces yield **completely distinct hashes**, proving why precomputed rainbow tables fail.

---

## 🏆 CTF Challenge Hashes (Included in Option 5)

Test your skills by cracking these real-world sample hashes:

| Challenge | Hash Type | Target Hash String | Clue / Attack Method |
| :--- | :--- | :--- | :--- |
| **Challenge 1** | MD5 | `5f4dcc3b5aa765d61d8327deb882cf99` | Common web password (Dictionary Attack) |
| **Challenge 2** | NTLM | `8846f7eaee8fb117ad06bdd830b7586c` | Windows SAM credential dump |
| **Challenge 3** | SHA-256 | `ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f` | Database user column |
| **Challenge 4** | NTLM | `2a7042a9b4009cf0ecf4fef8a38ec3aa` | Mutated corporate password based on `dragon` |

---

## 🛠️ Equivalent Industry Tooling Commands

If you have **Hashcat** or **John the Ripper** installed:

### Cracking Challenge 2 (NTLM) with Hashcat:
```bash
# Save hash to ntlm.hash
echo "8846f7eaee8fb117ad06bdd830b7586c" > ntlm.hash

# Run Hashcat in NTLM mode (-m 1000) using dictionary attack (-a 0)
hashcat -m 1000 -a 0 ntlm.hash phase-04-practical-ethical-hacking/wordlists/top-10000-passwords.txt
```

### Cracking with John the Ripper:
```bash
john --format=NT --wordlist=phase-04-practical-ethical-hacking/wordlists/top-10000-passwords.txt ntlm.hash
john --show --format=NT ntlm.hash
```
