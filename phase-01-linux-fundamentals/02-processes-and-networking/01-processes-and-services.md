# ⚙️ Step 4: Processes, Services & `/proc`

## 1. What is a Process?
Every program, command, script, or backdoor running on Linux is a **Process**.
Every process is assigned a unique number called a **PID (Process ID)**.

---

## 2. The Core Process Commands

| Command | What it does | Real-World Use |
| :--- | :--- | :--- |
| `ps aux` | Lists every single running process on the system | See what programs and background tasks are running |
| `ps aux | grep <name>` | Search for a specific running process (e.g., `grep python`) | Check if a web server, database, or tool is active |
| `top` | Interactive live task manager | See which process is eating CPU or memory |
| `kill <PID>` | Gracefully stops a process | Terminate a running script |
| `kill -9 <PID>` | Forcefully kills a process immediately | Stop an unresponsive or runaway task |

---

## 3. The Hacker's Secret: The `/proc` Directory

In Linux, process data is exposed as a directory inside `/proc/<PID>/`.

If an admin runs:
```bash
mysql -u root -pSecretP@ssw0rd123
```
Anyone on the system can inspect that process:
```bash
cat /proc/<PID>/cmdline
```
And they can read all environment variables (API keys, secret tokens) passed to that process:
```bash
cat /proc/<PID>/environ | tr '\0' '\n'
```
*(This is why passing passwords as command-line arguments is a major security flaw!)*

---

## 4. Services (Daemons) & `systemctl`

Programs that run automatically in the background (like web servers, SSH, databases) are called **services** (or daemons).

Modern Linux manages services using `systemctl`:
```bash
# Check if a service is running
systemctl status ssh

# Start or stop a service
systemctl start ssh
systemctl stop ssh

# Enable a service to start automatically on system boot
systemctl enable ssh
```
