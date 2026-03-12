import requests
import json

cep_input = input("digite o Cep ( somente numero ou formato):")
 
#removendo tudo que nao for numero
cep_limpo = ""
for caractere in cep_input:
    if caractere.isigit():
        cep_lmpo += caractere

#monta a url
url = f"https://iacep.com.br/ws/{cep_limpo}/json/"


#faz a requisiçao 
try:
    resposta = requests.get(url)
    if resposta.status_code == 200:
        #apenas mostra o texto puro da resposta (JSON cru)
    else:
        prnt("erro ao buscar o Cep. Codgo de status:", resposta.status_code)

except requests.exceptions.requestexection as e:
    print ("erro na requisiçao:", e)


