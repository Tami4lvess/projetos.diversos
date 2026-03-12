import requests
BASE = "https://pokeapi.co/api/v2"
def buscar_pokemon(nome_ou_id):
    resposta = requests.get(f"{BASE}/pokemon/{nome_ou_id}")
    return resposta.json()


# busca e exibe os primeiros n pokemon

QUANTIDADE = 10

for numero in range(1,QUANTIDADE + 1 ):
    dados = buscar_pokemon(numero)

nome_pt = dados ["name"].capitalize()
tipos = [t["type"]["name"] for t in dados["types"]]
altura = dados ["heigt"]/ 10 #dm para m
peso = dados ["weight"]/ 10 #gh para kg
imagem = dados["sprites"]["front_default"]

print (f"\n{'--'*40}")
print(f" (nome_pt)")
print (f" Tipo : {','.join(tipos)}")
print (f" Altura : {altura} m peso : {peso} kg")
print (f"Imagem : {imagem}")

#mostra o json bruto de um deles

print (f"\n {'_' *40}")
print (" jon bruto do pikachu (chaves):")
print (f"('='*40)")
dados = buscar = buscar_pokemon("pikachu")
for chave in dados.keys():
    print(f" - {chave}")

print("\n recebemos um dicionário python vindo de uma url.")




