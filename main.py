from colorama import Fore, Style
import portscan
import dns_lookup
import subdomain_enum
import whois_lookup
import wappalyzer

def menu():
    print(Fore.CYAN + "\nBem-vindo ao ReconApp!" + Style.RESET_ALL)
    print("1. Portscan")
    print("2. DNS Lookup")
    print("3. Enumeração de Subdomínios")
    print("4. WHOIS Lookup")
    print("5. Detectar Tecnologias (Wappalyzer)")
    print("6. Sair")

def main():
    while True:
        menu()
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            target = input("Digite o IP ou domínio para o portscan: ")
            portscan.run_portscan(target)
        elif choice == "2":
            domain = input("Digite o domínio: ")
            dns_lookup.run_dns_lookup(domain)
        elif choice == "3":
            domain = input("Digite o domínio: ")
            subdomain_enum.run_enum(domain)
        elif choice == "4":
            domain = input("Digite o domínio: ")
            whois_lookup.run_whois(domain)
        elif choice == "5":
            url = input("Digite a URL (com http:// ou https://): ")
            wappalyzer.run_wappalyzer(url)
        elif choice == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
