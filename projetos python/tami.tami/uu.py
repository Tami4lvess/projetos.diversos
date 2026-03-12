def switch_dia (dia):
    dias = {
            "segunda" : "inicio de semana",
            "quarta" : "meio de semana",
            "sabado" : "fm de semana"
    }
    return dias.get (dia.lower(), "dia invalido")
dia_usuario = "quarta"
print(f"o dia é {dia_usuario}:{switch_dia(dia_usuario)}")

                     