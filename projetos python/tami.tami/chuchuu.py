class contabancaria:
    def __init__(self,titular,saldoinicil):
        self.__titular=titular
        self.__saldo=titular
    def getsaldo(self):
        return self.__saldo
    def depositar(self,valor):
        if valor <=0:
            print("valor invalido")
        else:
            self.__saldo += valor
    def sacar (self,valor):
        if valor<=0:
            print ('valor invalido')
        elif valor> self.__saldo:
            print("pobre, seu saldo é insuficiente")
        else:
            self.__saldo-=valor

