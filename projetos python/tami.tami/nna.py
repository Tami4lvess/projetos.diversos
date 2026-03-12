def calcular_financiamento():
    print ("=====simulador de financiamento de carro=====\n")
#entrada de dados, esta declarando as variaveis

    valor_carro = float(input('informe o valor total do carro(R$):'))
    entrada = float(input("informe o valor da entrada (R$):"))
    taxa_juros_mensal= float(input("informe a taxa de juros mensal(%):"))
    meses = int(input("informe o numero de parcelas(meses):"))
#calculo
    
    valor_financiado = valor_carro - entrada

    i = taxa_juros_mensal / 100
    if taxa_juros_mensal > 2:
        print("taxa de juros abusia")
    else:
        print("txa de juros dentro do eperado")
#pmt = p* [i*(1+i)**n]/[(1+i)**n-1]
    if i == 0:
        prestacao = valor_financiado / meses
    else:
        prestacao = valor_financiado * (i*(1+i)** meses)/((1+i)**meses-1)


    total_pago = prestacao * meses

    juros_total = total_pago - valor_financiado

#saida de dados
    print ("\n===== Resultado da simulacao=====")
    print(f"valor do carro:R&{valor_carro:,.2f}")
    print(f"entrada:R${entrada:,.2f}")
    print(f"valor financiado:R${valor_financiado:,.2f}")
    print(f"prazo:{meses} meses")
    print(f"taxa de juros mensal:{taxa_juros_mensal:.2f}%")
    print(f"pretacao mensal:R${total_pago:,.2f}")
    print(f"total de juros pagos: R$ {juros_total:,.2f}")
    print("=================================")
#chamando a funcao
calcular_financiamento()
