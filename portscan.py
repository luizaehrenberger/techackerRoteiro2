import socket

def run_portscan(target):
    print(f"\nIniciando Portscan em {target}...")
    for port in range(20, 1025):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Porta {port} aberta")
            s.close()
        except Exception as e:
            print(f"Erro: {e}")
            break
