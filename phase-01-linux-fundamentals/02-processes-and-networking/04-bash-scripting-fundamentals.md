# 📜 Step 7: Bash Scripting Fundamentals for Security

Bash scripting is the glue of cybersecurity. Whether chaining command-line tools into an automated recon pipeline or writing payloads for initial access, mastering Bash syntax is essential.

---

## 1. Anatomy of a Robust Bash Script

```bash
#!/usr/bin/env bash

# Robust Execution Flags:
# -e : Exit immediately if any command fails
# -u : Treat unset variables as an error and exit
# -o pipefail : Catch failures anywhere in a pipeline (e.g. cmd1 | cmd2)
set -euo pipefail
```

---

## 2. Variables & Arguments

```bash
# Variable assignment (NO spaces around '=')
TARGET_IP="192.168.1.100"
SCAN_PORT=80

# Positional Parameters
SCRIPT_NAME="$0"    # Name of the script
FIRST_ARG="$1"      # First CLI argument passed
ALL_ARGS="$@"       # All arguments as a list
TOTAL_ARGS="$#"     # Count of arguments passed

# Default values if unset
PORT="${1:-80}"     # Use argument 1, or default to port 80
```

---

## 3. Conditionals & Tests

Use double brackets `[[ ... ]]` for modern Bash conditionals:

```bash
# Check if file exists
if [[ -f "/var/log/auth.log" ]]; then
    echo "[+] Found auth.log"
elif [[ -d "/var/log" ]]; then
    echo "[!] File missing, but directory exists"
else
    echo "[-] Log directory not found"
fi

# Common test operators:
# -f <file> : True if file exists and is a regular file
# -d <dir>  : True if directory exists
# -x <file> : True if file is executable
# -z <str>  : True if string is empty
# -n <str>  : True if string is NOT empty
# -eq, -ne, -lt, -gt : Numeric comparisons (e.g. [[ $# -eq 0 ]])
```

---

## 4. Loops

### For Loop (Iterating over lists/files)
```bash
for port in 21 22 80 443 8080; do
    echo "[*] Checking port: $port"
done
```

### While Loop (Streaming files line-by-line)
*Always use `IFS= read -r` to avoid stripping whitespace and backslashes:*
```bash
while IFS= read -r line; do
    echo "Processing line: $line"
done < "targets.txt"
```

---

## 5. Streams, Redirection & Pipelines

| Syntax | What it does |
| :--- | :--- |
| `cmd > output.txt` | Redirect standard output (stdout), overwriting file |
| `cmd >> output.txt` | Append stdout to file |
| `cmd 2> errors.txt` | Redirect standard error (stderr) |
| `cmd 2>&1` | Combine stderr into stdout |
| `cmd > /dev/null 2>&1` | Suppress all output (silent execution) |
| `cmd1 \| cmd2` | Pipe stdout of `cmd1` as stdin into `cmd2` |

---

## 6. Exit Codes & Error Handling

Every command in Linux returns an exit status between `0` and `255`:
* `0` = **Success**
* Non-zero (e.g. `1`, `127`) = **Error** / failure

```bash
ping -c 1 8.8.8.8 > /dev/null 2>&1
if [[ $? -eq 0 ]]; then
    echo "[✓] Internet connection is active!"
else
    echo "[X] Host unreachable!"
fi
```
