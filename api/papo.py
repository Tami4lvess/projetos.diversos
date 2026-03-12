import requests
import json

cep_input = input('Digite o CEP: ')
url = f"https://viacep.com.br/ws/{cep_input}/json/"
resposta = requests.get(url)

if resposta.status_code == 200:
    print(resposta.json())
else:
    print("Erro ao buscar o CEP")
