#!/bin/bash

echo "Criando ambiente virtual..."
python3 -m venv venv

echo "Ativando ambiente virtual..."
source venv/bin/activate

echo "Instalando dependências do projeto..."
pip install -r requirements.txt

echo "Ambiente configurado com sucesso!"
echo "Para ativar o ambiente manualmente depois, use: source venv/bin/activate"
