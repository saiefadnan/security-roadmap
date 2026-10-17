# 🕵️ Step 1: Passive Reconnaissance & OSINT

> **Phase 4: Practical Ethical Hacking**  
> *"The best recon is the recon the target never knows happened."*

---

## 1. Passive vs. Active Reconnaissance

| Feature | Passive Reconnaissance | Active Reconnaissance |
| :--- | :--- | :--- |
| **Direct Interaction** | **Zero.** Never sends a single packet to the target's servers. | **Direct.** Probes target ports and web applications. |
| **Detection Risk** | **Undetectable.** Target firewalls/SIEMs will never see your IP. | **Detectable.** Target firewalls log port scans and directory fuzzing. |
| **Information Source**| Public third-party databases, search engines, registrar records. | The live running target host itself. |
| **Key Tools** | Google Dorking, Shodan, WHOIS, Certificate Transparency, Wayback Machine. | Nmap, Gobuster, ffuf, Nikto, Netcat. |

---

## 2. Google Dorking (Advanced Search Operators)

Search engines have already crawled billions of public pages. Pentesters use **Google Dorks** to uncover sensitive information without alerting the target.

### Essential Operators:
- `site:domain.com` $\rightarrow$ Restrict search strictly to that domain.
- `filetype:ext` or `ext:ext` $\rightarrow$ Search for specific extensions (`pdf`, `xlsx`, `sql`, `env`, `log`).
- `inurl:keyword` $\rightarrow$ Search for strings inside the URL path (e.g. `inurl:admin`, `inurl:login`).
- `intitle:"text"` $\rightarrow$ Search for text inside the HTML page title (e.g. `intitle:"index of /"`).

### High-Value Pentest Dorks:
```text
# 1. Directory Listings (exposed folder browsing)
site:target.com intitle:"index of /"

# 2. Database Dumps & Backups accidentally left in web root
site:target.com filetype:sql OR filetype:bkp OR filetype:bak

# 3. Leaked Credentials & Environment Variables
site:target.com filetype:env "DB_PASSWORD"

# 4. Hidden Login & Admin Portals
site:target.com inurl:admin OR inurl:login OR inurl:portal
```

---

## 3. Shodan: The Search Engine for the Internet

**[Shodan](https://www.shodan.io)** continuously scans the global IPv4 address space, grabbing banners from every open port.

### Valuable Shodan Search Queries:
- `hostname:target.com` $\rightarrow$ Finds all IP addresses and servers tied to the domain.
- `org:"Target Organization"` $\rightarrow$ Finds all public IP ranges owned by that company.
- `port:21 "vsftpd 2.3.4"` $\rightarrow$ Finds vulnerable FTP servers across the world.
- `has_screenshot:true "Remote Desktop"` $\rightarrow$ Finds exposed Windows RDP screens with no password.

---

## 4. Domain & Certificate Intelligence

1. **WHOIS:** Queries public registrars for domain creation dates, registrant organizations, and DNS name servers:
   ```bash
   whois target.com | grep -iE "creation date|registrar:"
   ```
2. **Certificate Transparency (`crt.sh`):** Every public SSL certificate issued for subdomains is stored in append-only public logs, revealing unlinked subdomains like `staging.target.com`, `vpn.target.com`, or `api-dev.target.com`.
3. **The Wayback Machine (archive.org):** Lets you view older versions of the website from 5 or 10 years ago to find deleted documentation, old employee directories, or deprecated endpoints.
