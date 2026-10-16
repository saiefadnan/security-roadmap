# 👤 Step 2: Understanding `/etc/passwd` & Users

Every line in `/etc/passwd` has exactly **7 fields**, separated by colons (`:`):

```text
root : x : 0 : 0 : root : /root : /bin/bash
 │    │   │   │     │      │        │
 │    │   │   │     │      │        └─ 7. Default Shell (e.g. /bin/bash, /usr/sbin/nologin)
 │    │   │   │     │      └────────── 6. Home Directory
 │    │   │   │     └───────────────── 5. User Description (GECOS)
 │    │   │   └─────────────────────── 4. Group ID (GID)
 │    │   └─────────────────────────── 3. User ID (UID) -> UID 0 is always ROOT
 │    └─────────────────────────────── 2. Password Placeholder ('x' means hash is in /etc/shadow)
 └──────────────────────────────────── 1. Username
```

---

## 🔍 The Pentester's Eye: What to Look For

### 1. Interactive Users vs Service Accounts
Look at the last field (the shell):
* `/bin/bash` or `/bin/sh` → A real user account that can log in and get a terminal.
* `/usr/sbin/nologin` or `/bin/false` → System/service accounts (like `mail`, `games`, `daemon`). They exist only to run background tasks, not for humans to log into.

**Pentester One-Liner to find all log-in capable users:**
```bash
grep -E "(/bin/bash|/bin/sh)" /etc/passwd
```

---

### 2. Why is the password field just `x`?
Back in the 1980s, password hashes were stored right here in `/etc/passwd`. Because every program needs to read user names, `/etc/passwd` must be readable by everyone. Anyone on the machine could copy the hashes and crack them offline.

Unix fixed this by moving the actual hashes to `/etc/shadow`, which is readable **only by root**.
