#!/usr/bin/env python3
"""
=============================================================================
  HASH CRACKING & CREDENTIAL SECURITY LAB (Interactive Hands-on Engine)
=============================================================================
Demonstrates how offline hash cracking works under the hood:
1. NTLM, MD5, SHA-256, and Salted Hash Generation.
2. High-speed Dictionary Attacks (simulating Hashcat -a 0).
3. Rule-Based Mutation Attacks (simulating Hashcat rules: leetspeak, years, caps).
4. The Salt Defense Experiment (why salts defeat rainbow tables).
=============================================================================
"""

import hashlib
import binascii
import struct
import time
import sys
import os

# --- Pure Python RFC 1320 MD4 Implementation (ensures NTLM works everywhere) ---

def _md4(data: bytes) -> bytes:
    """Pure Python MD4 implementation (RFC 1320) for 100% cross-platform NTLM support."""
    def F(x, y, z): return (x & y) | (~x & z)
    def G(x, y, z): return (x & y) | (x & z) | (y & z)
    def H(x, y, z): return x ^ y ^ z
    def lrot(val, n): return ((val << n) & 0xffffffff) | (val >> (32 - n))

    msg = bytearray(data)
    orig_len_bits = (len(msg) * 8) & 0xffffffffffffffff
    msg.append(0x80)
    while len(msg) % 64 != 56:
        msg.append(0x00)
    msg += struct.pack('<Q', orig_len_bits)

    A, B, C, D = 0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476

    for i in range(0, len(msg), 64):
        X = list(struct.unpack('<16I', msg[i:i+64]))
        AA, BB, CC, DD = A, B, C, D

        # Round 1
        s1 = [3, 7, 11, 19]
        for j in range(16):
            idx = j
            A = lrot((A + F(B, C, D) + X[idx]) & 0xffffffff, s1[j % 4])
            A, B, C, D = D, A, B, C

        # Round 2
        s2 = [3, 5, 9, 13]
        order2 = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]
        for j in range(16):
            idx = order2[j]
            A = lrot((A + G(B, C, D) + X[idx] + 0x5a827999) & 0xffffffff, s2[j % 4])
            A, B, C, D = D, A, B, C

        # Round 3
        s3 = [3, 9, 11, 15]
        order3 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        for j in range(16):
            idx = order3[j]
            A = lrot((A + H(B, C, D) + X[idx] + 0x6ed9eba1) & 0xffffffff, s3[j % 4])
            A, B, C, D = D, A, B, C

        A = (A + AA) & 0xffffffff
        B = (B + BB) & 0xffffffff
        C = (C + CC) & 0xffffffff
        D = (D + DD) & 0xffffffff

    return struct.pack('<4I', A, B, C, D)

# --- Core Hashing Algorithms ---

def hash_md5(plaintext: str) -> str:
    return hashlib.md5(plaintext.encode('utf-8')).hexdigest()

def hash_sha256(plaintext: str) -> str:
    return hashlib.sha256(plaintext.encode('utf-8')).hexdigest()

def hash_ntlm(plaintext: str) -> str:
    """
    Windows NTLM Hash: MD4(UTF-16LE(password))
    Notice: No salt!
    """
    try:
        return hashlib.new('md4', plaintext.encode('utf-16le')).hexdigest()
    except Exception:
        # Fallback to pure Python MD4
        return binascii.hexlify(_md4(plaintext.encode('utf-16le'))).decode('ascii')

def hash_salted(plaintext: str, salt: str) -> str:
    """Simulates salted Linux/web password hashing: SHA256(salt + password)"""
    return hashlib.sha256((salt + plaintext).encode('utf-8')).hexdigest()

# --- Attack Engines ---

def dictionary_attack(target_hash: str, hash_type: str, wordlist_path: str):
    print(f"\n[*] Starting Dictionary Attack on [{hash_type.upper()}] hash: {target_hash}")
    print(f"[*] Reading wordlist: {wordlist_path}")
    
    if not os.path.exists(wordlist_path):
        print(f"[!] Error: Wordlist not found at {wordlist_path}")
        return

    hash_fn = {
        'md5': hash_md5,
        'sha256': hash_sha256,
        'ntlm': hash_ntlm
    }.get(hash_type.lower())

    if not hash_fn:
        print(f"[!] Unsupported hash type: {hash_type}")
        return

    start_time = time.time()
    count = 0
    cracked = None

    with open(wordlist_path, 'r', encoding='latin-1', errors='ignore') as f:
        for line in f:
            candidate = line.strip()
            count += 1
            if hash_fn(candidate) == target_hash.lower():
                cracked = candidate
                break

    elapsed = time.time() - start_time
    rate = count / elapsed if elapsed > 0 else count

    print("-" * 65)
    if cracked:
        print(f"  [+] HASH CRACKED! Password: \033[92m{cracked}\033[0m")
        print(f"  [+] Attempts: {count:,} words checked")
        print(f"  [+] Time: {elapsed:.4f} seconds ({rate:,.0f} hashes/sec)")
    else:
        print(f"  [-] Hash NOT found in wordlist ({count:,} words exhausted)")
        print(f"  [-] Time: {elapsed:.4f} seconds")
    print("-" * 65)

def rule_mutation_attack(target_hash: str, hash_type: str, base_word: str):
    """
    Demonstrates Hashcat's rule engine.
    Takes a base word (e.g., 'password') and generates real-world permutations:
    - Capitalization (Password, PASSWORD)
    - Years (Password2024, Password2025, Password2026)
    - Exclamations / Symbols (Password!, Password123!)
    - Leetspeak (p@ssw0rd, P@ssw0rd123)
    """
    print(f"\n[*] Generating Rule-Based Mutations for base word: '{base_word}'")
    hash_fn = {'md5': hash_md5, 'sha256': hash_sha256, 'ntlm': hash_ntlm}.get(hash_type.lower(), hash_md5)

    mutations = set()
    variations = [base_word, base_word.capitalize(), base_word.upper()]
    
    # Leetspeak rules
    leet_map = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$'}
    leet_word = base_word
    for k, v in leet_map.items():
        leet_word = leet_word.replace(k, v)
    variations.extend([leet_word, leet_word.capitalize()])

    suffixes = ['', '1', '123', '!', '123!', '2024', '2025', '2026', '@123', '@123!', '@2025', '@2026', '!@#', '$$$']
    for var in variations:
        for suf in suffixes:
            mutations.add(var + suf)

    print(f"[*] Testing {len(mutations)} mutated combinations against: {target_hash}")
    cracked = None
    for cand in mutations:
        if hash_fn(cand) == target_hash.lower():
            cracked = cand
            break

    print("-" * 65)
    if cracked:
        print(f"  [+] MUTATION CRACKED! Password: \033[92m{cracked}\033[0m")
        print(f"  [+] Matched Rule Mutation: '{cracked}' from base '{base_word}'")
    else:
        print("  [-] No matching mutation found.")
    print("-" * 65)

def salt_defense_demo():
    """Demonstrates why salts completely destroy rainbow tables and mass-lookup attacks."""
    password = "SuperSecretPassword123"
    print("\n=======================================================")
    print("   THE SALT EXPERIMENT: UNSALTED vs SALTED HASHING")
    print("=======================================================")
    print(f"Target Password shared by 3 different employees: '{password}'\n")

    print("[1] UNSALTED NTLM (Windows Default Flaw):")
    ntlm1 = hash_ntlm(password)
    ntlm2 = hash_ntlm(password)
    ntlm3 = hash_ntlm(password)
    print(f"  * Alice NTLM: {ntlm1}")
    print(f"  * Bob   NTLM: {ntlm2}")
    print(f"  * Carol NTLM: {ntlm3}")
    print("  --> ALL THREE HASHES ARE IDENTICAL!")
    print("  --> Consequence: An attacker cracks ONE hash, and instantly owns ALL THREE accounts!\n")

    print("[2] SALTED HASHES (Linux / Modern Web Backends):")
    salt1, salt2, salt3 = "9kF2!", "xL7#q", "pM4$v"
    s_hash1 = hash_salted(password, salt1)
    s_hash2 = hash_salted(password, salt2)
    s_hash3 = hash_salted(password, salt3)
    print(f"  * Alice (Salt: {salt1}): {s_hash1}")
    print(f"  * Bob   (Salt: {salt2}): {s_hash2}")
    print(f"  * Carol (Salt: {salt3}): {s_hash3}")
    print("  --> ALL THREE HASHES ARE COMPLETELY DIFFERENT!")
    print("  --> Consequence: Cracking Alice reveals NOTHING about Bob or Carol.")
    print("      Precomputed Rainbow Tables are rendered 100% USELESS.")
    print("=======================================================\n")

def main():
    default_wordlist = os.path.join(os.path.dirname(__file__), "..", "wordlists", "top-10000-passwords.txt")
    if not os.path.exists(default_wordlist):
        default_wordlist = os.path.join(os.path.dirname(__file__), "..", "wordlists", "passwords.txt")

    print("""
  ╔══════════════════════════════════════════════════════╗
  ║    PRACTICAL HASH CRACKING & CREDENTIAL LAB          ║
  ║         Educational Offline Attack Engine            ║
  ╚══════════════════════════════════════════════════════╝
    """)

    while True:
        print("\nSelect an action:")
        print("  1) Generate a Hash (NTLM, MD5, SHA-256)")
        print("  2) Run Dictionary Attack (Cracking Wordlist)")
        print("  3) Run Rule Mutation Attack (Cracking Permutations)")
        print("  4) Run Salt Defense Experiment")
        print("  5) Solve CTF Challenge Hashes")
        print("  0) Exit")

        choice = input("\nChoice > ").strip()

        if choice == '1':
            pw = input("Enter password to hash: ").strip()
            print(f"\n  MD5:     {hash_md5(pw)}")
            print(f"  SHA-256: {hash_sha256(pw)}")
            print(f"  NTLM:    {hash_ntlm(pw)}")

        elif choice == '2':
            h = input("Enter target hash: ").strip()
            ht = input("Hash type (md5 / sha256 / ntlm) [default: ntlm]: ").strip() or "ntlm"
            dictionary_attack(h, ht, default_wordlist)

        elif choice == '3':
            h = input("Enter target hash: ").strip()
            ht = input("Hash type (md5 / sha256 / ntlm) [default: ntlm]: ").strip() or "ntlm"
            base = input("Enter suspected base word (e.g. 'summer', 'admin', 'dragon'): ").strip()
            rule_mutation_attack(h, ht, base)

        elif choice == '4':
            salt_defense_demo()

        elif choice == '5':
            print("\n--- CTF CHALLENGE HASHES ---")
            challenges = [
                ("Challenge 1 (MD5)", "5f4dcc3b5aa765d61d8327deb882cf99", "md5"),
                ("Challenge 2 (NTLM)", "8846f7eaee8fb117ad06bdd830b7586c", "ntlm"),
                ("Challenge 3 (SHA-256)", "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f", "sha256"),
                ("Challenge 4 (NTLM - Mutated 'dragon')", "2a7042a9b4009cf0ecf4fef8a38ec3aa", "ntlm")
            ]
            for idx, (title, ch_hash, htype) in enumerate(challenges, 1):
                print(f"  [{idx}] {title}: {ch_hash}")

            sub = input("\nSelect challenge number to crack (1-4) or 'all': ").strip()
            to_run = challenges if sub.lower() == 'all' else [challenges[int(sub)-1]] if sub in ['1','2','3','4'] else []
            for title, ch_hash, htype in to_run:
                print(f"\n>>> Cracking {title}...")
                dictionary_attack(ch_hash, htype, default_wordlist)
                if ch_hash == "2a7042a9b4009cf0ecf4fef8a38ec3aa":
                    rule_mutation_attack(ch_hash, htype, "dragon")

        elif choice == '0':
            print("Exiting lab.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
