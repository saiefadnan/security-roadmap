# 🌐 Step 5: Package Management & Network Ports (`ss`, `curl`, `ip`)

## 1. Package Management (`apt`)
On Debian/Ubuntu, software is managed with **APT (Advanced Package Tool)**:

```bash
# 1. Update package list from repositories
apt update

# 2. Install a package (e.g., OpenSSH server, curl, net-tools)
apt install -y openssh-server curl net-tools

# 3. Remove a package
apt remove <package-name>
```

---

## 2. Network Ports & Sockets: The Golden Command (`ss`)

In cybersecurity, checking what ports are **listening** on a target tells you what services are exposed to the outside world.

```bash
ss -tulpn
```

### Breakdown of the flags:
* `-t` → **TCP** ports
* `-u` → **UDP** ports
* `-l` → Only **Listening** ports (waiting for connections)
* `-p` → Show the **Process / Program** name and PID
* `-n` → Don't resolve names, show **Numeric** port numbers (e.g. `22` instead of `ssh`)

### Common Well-Known Ports:
* `21` → FTP
* `22` → SSH (Secure Shell)
* `25` → SMTP (Email)
* `53` → DNS
* `80` → HTTP (Unencrypted web)
* `443` → HTTPS (Encrypted web)
* `3306` → MySQL Database
* `5432` → PostgreSQL Database

---

## 3. Network Interfaces & IPs (`ip`)

To see your machine's IP address and network interfaces:

```bash
# Detailed view:
ip a

# Clean, brief colored view:
ip -br -c a
```
