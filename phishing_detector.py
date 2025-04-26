import requests
import tldextract
import re
from urllib.parse import urlparse
from colorama import Fore, Style, init

init(autoreset=True)  # For colored output

# Suspicious TLDs
suspicious_tlds = ['zip', 'xyz', 'buzz', 'top', 'gq', 'tk', 'ml']

# Suspicious keywords
keywords = ['login', 'secure', 'account', 'update', 'verify', 'bank', 'confirm', 'signin', 'paypal', 'ebay', 'webscr']

def is_https(url):
    try:
        response = requests.get(url, timeout=5)
        return response.url.startswith('https')
    except:
        return False

def suspicious_keywords(url):
    return [kw for kw in keywords if kw in url.lower()]

def suspicious_tld(url):
    ext = tldextract.extract(url)
    return ext.suffix in suspicious_tlds

def is_ip_address(url):
    parsed = urlparse(url)
    hostname = parsed.hostname
    if hostname:
        return bool(re.match(r'^\d{1,3}(\.\d{1,3}){3}$', hostname))
    return False

def url_length_check(url):
    return len(url) > 75  # Generally, URLs longer than 75 are suspicious

def check_url(url):
    result = {}
    result['https'] = is_https(url)
    result['suspicious_keywords'] = suspicious_keywords(url)
    result['suspicious_tld'] = suspicious_tld(url)
    result['ip_address'] = is_ip_address(url)
    result['url_length'] = url_length_check(url)

    # Calculate Risk Score
    risk_score = 0
    if not result['https']:
        risk_score += 30
    if result['suspicious_keywords']:
        risk_score += len(result['suspicious_keywords']) * 10
    if result['suspicious_tld']:
        risk_score += 20
    if result['ip_address']:
        risk_score += 20
    if result['url_length']:
        risk_score += 10

    result['risk_score'] = min(risk_score, 100)  # Max 100

    return result

def main():
    url = input("🔗 Enter the URL to scan: ")
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    analysis = check_url(url)

    print(f"\n📋 {Fore.CYAN}Analysis for {url}{Style.RESET_ALL}")
    print(f"🔒 Uses HTTPS: {Fore.GREEN if analysis['https'] else Fore.RED}{'Yes' if analysis['https'] else 'No'}")
    print(f"🕵️ Suspicious Keywords: {Fore.RED if analysis['suspicious_keywords'] else Fore.GREEN}{analysis['suspicious_keywords'] or 'None'}")
    print(f"🌐 Suspicious TLD: {Fore.RED if analysis['suspicious_tld'] else Fore.GREEN}{'Yes' if analysis['suspicious_tld'] else 'No'}")
    print(f"📄 URL uses IP Address: {Fore.RED if analysis['ip_address'] else Fore.GREEN}{'Yes' if analysis['ip_address'] else 'No'}")
    print(f"🔗 URL Length > 75 characters: {Fore.RED if analysis['url_length'] else Fore.GREEN}{'Yes' if analysis['url_length'] else 'No'}")
    print(f"⚡ Risk Score: {Fore.YELLOW}{analysis['risk_score']} / 100{Style.RESET_ALL}")

    if analysis['risk_score'] >= 50:
        print(f"{Fore.RED}⚠️ Warning: This site looks suspicious!")
    else:
        print(f"{Fore.GREEN}✅ This site looks safe (basic checks only).")

if __name__ == "__main__":
    main()
