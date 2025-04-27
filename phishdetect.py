#!/usr/bin/env python3
import argparse
from colorama import Fore, Style, init
import tldextract
import ssl
import socket
import urllib.parse
import time

# Initialize colorama
init(autoreset=True)

# Banner
def banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
   ____  _     _     _     _             
  |  _ \| |__ (_)___| |__ (_)_ __   __ _  
  | |_) | '_ \| / __| '_ \| | '_ \ / _` | 
  |  __/| | | | \__ \ | | | | | | | (_| | 
  |_|   |_| |_|_|___/_| |_|_|_| |_|\__, | 
                                   |___/  
        🛡️ Phishing URL Detector 🛡️
    """)
    time.sleep(1)

# SSL Checking
def check_ssl(hostname):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.settimeout(3)
            s.connect((hostname, 443))
            s.getpeercert()
        return True
    except Exception:
        return False

# URL Analysis
def analyze_url(url):
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.netloc or parsed_url.path

    ssl_status = check_ssl(hostname)
    extracted = tldextract.extract(url)
    domain = extracted.domain.lower()
    suffix = extracted.suffix.lower()
    subdomain = extracted.subdomain.lower()

    suspicious_keywords = ['login', 'secure', 'account', 'update', 'verify', 'bank', 'paypal', 'signin']
    suspicious_tlds = ['xyz', 'top', 'club', 'online', 'site']

    score = 0
    reasons = []

    for keyword in suspicious_keywords:
        if keyword in url.lower():
            score += 1
            reasons.append(f"Contains suspicious keyword: {keyword}")

    if suffix in suspicious_tlds:
        score += 1
        reasons.append(f"Suspicious TLD detected: .{suffix}")

    if not ssl_status:
        score += 2
        reasons.append("SSL certificate is missing or invalid")

    if len(subdomain.split('.')) > 2:
        score += 1
        reasons.append(f"Unusual subdomain structure: {subdomain}")

    return score, reasons

# Main Execution
def main():
    parser = argparse.ArgumentParser(description="🛡️  Phishing URL Detector")
    parser.add_argument("url", help="URL to scan for phishing")
    args = parser.parse_args()

    banner()
    print(Fore.CYAN + "\n🔍 Scanning URL:", Fore.YELLOW + args.url)
    print(Fore.CYAN + "--------------------------------------------\n")

    score, reasons = analyze_url(args.url)

    if score >= 3:
        print(Fore.RED + Style.BRIGHT + "[!] ALERT: This URL is likely a phishing attempt!\n")
    elif score == 2:
        print(Fore.YELLOW + Style.BRIGHT + "[!] WARNING: This URL is suspicious, caution advised.\n")
    else:
        print(Fore.GREEN + Style.BRIGHT + "[+] SAFE: This URL looks clean.\n")

    print(Fore.MAGENTA + "🧠 Analysis Report:")
    for reason in reasons:
        print(Fore.YELLOW + "- " + reason)

    print(Fore.CYAN + "\n✅ Scan Completed.\n")

if __name__ == "__main__":
    main()
