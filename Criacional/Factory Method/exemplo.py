from concrete_factory import *
from abstract_product import *

class Teste:
    def __init__(self):
        self.guitarra = None
    
    def escolha(self) -> None:
        escolha = None
        while True:
            try:
                opcao = int(input("\nInforme a opção desejada! + \n1-Gibson Les Paul \n2-Gibson SG \n"+
                    "3-Fender Statocaster \n4-Fender Telecaster \n")) - 1
                tipo = Tipo(opcao)
                self.guitarra = Factory.new().guitarra(tipo)
                print("Marca: " + self.guitarra.marca() + " - Ano de Fabricação: "
                    + str(self.guitarra.ano_fabricacao()) + " - Modelos: ")
                for modelo in self.guitarra.modelo():
                    print(modelo)
            except: 
                break

Teste().escolha()