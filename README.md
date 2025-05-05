# ReconApp - Documentação e Relatório

## Sobre o Projeto
ReconApp é um aplicativo em linha de comando (CLI) para auxiliar na fase de reconhecimento de alvos em pentests. Ele é modular, extensível e fácil de usar.

## Funcionalidades
- Portscan (varredura de portas TCP)
- DNS Lookup
- Enumeração de Subdomínios
- WHOIS Lookup
- Detecção de tecnologias com Wappalyzer (via CLI)

## Requisitos
- Python 3.10+
- pip
- Bibliotecas:
  - requests
  - colorama
  - python-whois
- Para Wappalyzer: Node.js + `npm install -g wappalyzer`

## 1. Respostas às Perguntas de Pesquisa

### 1.1 Cinco ferramentas úteis para reconhecimento
- **theHarvester**: coleta e-mails, domínios e hosts públicos. Ideal para engenharia social.
- **Shodan**: pesquisa dispositivos IoT e servidores expostos. Muito usada para avaliar riscos remotos.
- **WHOIS**: identifica donos de domínios. Ajuda a rastrear origem de alvos.
- **Sublist3r / Amass**: ferramentas para encontrar subdomínios de um alvo.
- **Wappalyzer CLI**: detecta frameworks, CMSs e linguagens em uso no site.

### 1.2 Diferença entre SYN Scan e TCP Connect
- **SYN Scan**: envia pacotes SYN e observa a resposta. É rápido e discreto, mas requer acesso root.
- **TCP Connect**: realiza conexão completa (3-way handshake). Mais detectável, mas funciona sem permissão especial.

### 1.3 Como evitar detecção por IPS
- Reduzir velocidade de scan (evita detecção por anomalia de tráfego).
- Usar proxies e VPNs.
- Fragmentação de pacotes (ex: com `fragroute`).
- Rodar scans em horários de pico de tráfego.

## 2. Arquitetura do Sistema
O ReconApp segue um modelo modular:

````

main.py
\|- portscan.py
\|- dns\_lookup.py
\|- subdomain\_enum.py
\|- whois\_lookup.py
\|- wappalyzer.py

```

Cada módulo é responsável por uma funcionalidade. O `main.py` atua como controladora e interface do usuário.

## 3. Análise das Ferramentas Integradas
- **PortScan**: simples e eficaz. Utiliza `socket` com `connect_ex()` para detecção de portas abertas.
- **DNS Lookup**: resolve domínios para IPs usando `socket.gethostbyname()`.
- **Subdomain Enum**: tenta subdomínios comuns e verifica via `requests`.
- **WHOIS**: usa `python-whois` para obter dados públicos.
- **Wappalyzer CLI**: fornece insights rápidos sobre tecnologias web.


## 5. Considerações Finais
O ReconApp se mostrou eficaz como ferramenta de reconhecimento. Sua arquitetura modular facilita a manutenção e expansão. Todas as ferramentas integradas funcionaram corretamente nos testes realizados.
```

---

## Mock de Screenshot CLI

Bem-vindo ao ReconApp!
1. Portscan
2. DNS Lookup
3. Enumeração de Subdomínios
4. WHOIS Lookup
5. Detectar Tecnologias (Wappalyzer)
6. Sair
Escolha uma opção: 
