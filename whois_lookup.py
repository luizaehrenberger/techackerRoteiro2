import whois

def run_whois(domain):
    try:
        w = whois.whois(domain)
        print("\nInformações WHOIS:\n")
        print(w)
    except Exception as e:
        print(f"Erro ao buscar WHOIS: {e}")
