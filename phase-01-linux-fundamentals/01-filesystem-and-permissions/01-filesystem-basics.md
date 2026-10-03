# 📁 Step 1: The Linux Filesystem & Navigation

## 1. Why this matters in Cybersecurity
In Windows, you have drive letters like `C:\` and `D:\`.
In Linux, **everything exists under one single root folder: `/`**.

When an attacker gains a remote shell or a pentester audits a Linux server, there is no graphical desktop. You must know exactly where critical files live:

| Path | Purpose | Why Pentesters Care |
| :--- | :--- | :--- |
| `/` | The Root Directory | Top-level folder of the entire operating system. |
| `/etc` | System Configurations | Contains `/etc/passwd` (users list), `/etc/shadow` (password hashes), `/etc/hosts`, and network settings. |
| `/home` | Normal User Data | Where user personal files and SSH keys live (`/home/username/.ssh/`). |
| `/root` | Root (Admin) Home | Superuser's home directory. Only accessible by root. |
| `/var/log` | System & Security Logs | Contains `auth.log`, `syslog`, `nginx/`, `apache2/` records of logins and actions. |
| `/tmp` | Temporary Files | World-writable folder (`rwxrwxrwt`). Common staging ground to download tools/scripts. |
| `/bin` & `/sbin` | Essential Binaries | Standard commands (`ls`, `cat`, `ip`, `reboot`, etc.). |
| `/proc` | Virtual Kernel / Processes | Dynamic information about currently running processes and system memory. |

---

## 2. Essential Commands to Practice

Try each command in your WSL terminal:

```bash
# 1. Print your current directory
pwd

# 2. Go to the root of the entire Linux system
cd /

# 3. List the top-level folders with permissions and details
ls -la

# 4. Check the users defined on this system (first 10 lines)
head -n 10 /etc/passwd

# 5. Navigate back to our project folder on Windows (E: drive)
cd /mnt/e/my_projects/hack/phase-01-linux-fundamentals
```
