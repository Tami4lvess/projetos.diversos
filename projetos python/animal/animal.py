from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def emitirsom(self):
        pass 

class gato(animal):
    def emitirsom(self):
        return print("Miau Miau")
    
class cachorro(animal):
    def emitirsom(self):
        return print("Au Au")
    
def main():
    cat = gato
    cat.emitirsom()

if __name__ == '__animal__':
   main()

class pomba(animal):
    def emitirsom(self, nome):
        return print ("ruuuuh ruuuuuuuuh")