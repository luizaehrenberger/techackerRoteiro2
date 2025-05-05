import subprocess

def run_wappalyzer(url):
    print("Executando Wappalyzer CLI (requer instalação prévia)...")
    try:
        result = subprocess.run(['wappalyzer', url], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print("Erro: Wappalyzer CLI não encontrado. Instale com 'npm install -g wappalyzer'.")
