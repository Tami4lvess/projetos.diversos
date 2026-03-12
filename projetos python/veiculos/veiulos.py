class veiculos:
    def __init__(self,rodas,marca,modelo,ano):
        self.rodas = rodas
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def exibirinformacoes(self):
        print(f"{self.modelo}, ano:{self.ano}, rodas: {self.rodas}")
    def andar(self):
        print("ande carro:", self.modelo)
    def frear(self):
        print("pare o crro:", self.modelo)

class moto(veiculos):
    def __init__ (self,rodas,marca,modelo,ano,cilindrada):
        super(). __init__(rodas,marca,modelo,ano)
        self.cilindrada = cilindrada

class caminhao(veiculos):
    def __init__(self,rodas,marca,modelo,ano,limitecarga,nomecondutor):
        
