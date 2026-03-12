import requests
import json
cep_input = input('Digite o cep: ')
print("0 - Estado")
print("1- Nome da Rua")
print("2- Cidade")
print("3- ")
infodesejada = int(input("qual informação deseja saber?: "))
url = f"https://viacep.com.br/ws/{cep_input}/json"
resposta = requests.get(url)

if resposta.status_code == 200:
    match infodesejada:
        case 0:
            print("Estado:", requests["uf"])
        case 1:
            print("la")
        case 2:
            print("la")
        case 3:
            print(resposta.json())
else:
    print ("erro ao buscar o cep")