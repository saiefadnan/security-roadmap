# 🔐 Step 3: File Permissions & Octal Math (`chmod`)

In Linux, every file and directory has 3 sets of permissions:

```text
-  rwx  r-x  r--
│  ───  ───  ───
│   ▲    ▲    ▲
│   │    │    └── 3. Others (anyone else on the machine)
│   │    └─────── 2. Group  (members of the file's assigned group)
│   └──────────── 1. User   (the owner of the file)
└──────────────── File type: '-' is a normal file, 'd' is a directory
```

---

## 🧮 The Simple Math Behind `chmod`

Instead of typing letters, Linux uses numbers. Each permission has a value:

| Permission | Symbol | Value |
| :--- | :---: | :---: |
| **Read** | `r` | **4** |
| **Write** | `w` | **2** |
| **Execute** | `x` | **1** |
| **None** | `-` | **0** |

Add them together to get the number:
* `rwx` = $4 + 2 + 1$ = **7** (Full access)
* `rw-` = $4 + 2 + 0$ = **6** (Read + Write)
* `r-x` = $4 + 0 + 1$ = **5** (Read + Execute)
* `r--` = $4 + 0 + 0$ = **4** (Read only)
* `---` = $0 + 0 + 0$ = **0** (No access at all)

### Common Examples in Security:
* `chmod 777 file` → **Danger!** Everyone can read, modify, or run it.
* `chmod 755 script.sh` → Owner can do everything (`7`), everyone else can read and run it (`5`). Standard for tools and scripts.
* `chmod 600 id_rsa` → **Private!** Only the owner can read/write (`6`), nobody else has any access (`00`). Required for SSH private keys.
* `chmod 640 /etc/shadow` → Owner (`root`) can read/write (`6`), group (`shadow`) can read (`4`), others have zero access (`0`).
