# 🔐 Step 6: SSH Hardening & Environment Variables

Understanding remote access protocols and environment configurations is crucial for both system defense and post-exploitation.

---

## 1. SSH (Secure Shell) Architecture

SSH encrypts all traffic between a client and server. It operates on TCP port `22` by default.

### Key Authentication Workflow
Instead of brute-forceable passwords, modern security mandates **asymmetric key pairs**:
1. **Private Key (`id_ed25519`):** Stored only on your local client machine. **Never share this!**
2. **Public Key (`id_ed25519.pub`):** Placed on the remote server inside `~/.ssh/authorized_keys`.

```bash
# Generate a modern, secure ED25519 SSH keypair
ssh-keygen -t ed25519 -C "admin@security-lab"

# Copy your public key to the remote server automatically
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@192.168.1.50
```

### Critical Permission Boundaries (SSH Strict Modes)
OpenSSH actively refuses key authentication if permissions are too permissive (to prevent local users from tampering with your keys):
```bash
chmod 700 ~/.ssh                  # Only owner can read/write/enter directory
chmod 600 ~/.ssh/authorized_keys  # Only owner can read/write authorized keys
chmod 600 ~/.ssh/id_ed25519       # Only owner can read private key
```

### Server Hardening (`/etc/ssh/sshd_config`)
As a security administrator, apply these baseline hardening settings:
```text
# Disable direct root login over SSH
PermitRootLogin no

# Disable weak password logins (force key-based auth)
PasswordAuthentication no

# Limit maximum authentication attempts to deter brute-force
MaxAuthTries 3

# Disallow empty passwords
PermitEmptyPasswords no
```
*Apply changes with:* `sudo systemctl restart ssh`

---

## 2. Environment Variables

Environment variables are dynamic values loaded into every shell session that dictate how programs execute.

| Command | Action |
| :--- | :--- |
| `printenv` or `env` | View all active environment variables |
| `echo $PATH` | View directories searched when you execute a command |
| `export SECRET_KEY="value"` | Define an environment variable for the current session and child processes |
| `unset SECRET_KEY` | Remove an environment variable |

### Where are Environment Variables Defined?
* **System-wide:** `/etc/environment` and `/etc/profile.d/*.sh`
* **User-specific:** `~/.bashrc`, `~/.bash_profile`, or `~/.profile`

---

## 3. Security Implications (Offensive & Defensive)

### A. Secret & Credential Leakage
Many containerized applications and developers mistakenly store API tokens, database credentials, or AWS keys in environment variables:
```bash
# An attacker with command execution can immediately inspect:
cat /proc/$PID/environ | tr '\0' '\n'
```

### B. PATH Hijacking (Privilege Escalation)
When you type `ls`, Linux searches directories listed in `$PATH` from left to right (e.g., `/usr/local/bin:/usr/bin:/bin`).
If a script runs with `sudo` or SUID privileges and calls a binary without an absolute path (e.g. `service nginx restart` instead of `/usr/sbin/service`), an attacker who can modify `$PATH` or write to a prioritized folder can inject a malicious script named `service`:
```bash
export PATH=/tmp:$PATH
# If /tmp/service exists and is executable, the system executes the attacker's script!
```

### C. Sudo Environment Preservation (`sudo -E`)
By default, `sudo` strips out dangerous environment variables (`secure_path`). However, if `/etc/sudoers` specifies `env_keep += "LD_PRELOAD"` or allows `sudo -E`, a user can hijack shared libraries to escalate privileges to root.
