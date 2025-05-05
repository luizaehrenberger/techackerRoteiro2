import socket

def run_dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"Endereço IP de {domain}: {ip}")
    except socket.gaierror:
        print("Domínio inválido ou sem DNS.")
