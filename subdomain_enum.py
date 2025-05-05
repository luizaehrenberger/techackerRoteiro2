import requests

def run_enum(domain):
    subdomains = ["www", "mail", "ftp", "test", "blog", "dev"]
    print(f"Enumerando subdomínios de {domain}...")
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=2)
            print(f"[+] Encontrado: {url}")
        except requests.ConnectionError:
            pass
