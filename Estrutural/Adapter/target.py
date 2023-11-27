"""Module que representa a classe alvo do padrão Adapter"""
from abstracts import IPassaro

class Pato(IPassaro):
    """Classe que representa um pato"""
    def __init__(self, nome:str):
        """Cria um novo pato"""
        self.__nome = nome

    @classmethod
    def new(cls: "Pato", nome:str) -> IPassaro:
        """Cria um novo pato"""
        return cls(nome)
        
    def voar(self) ->str:
        """Retorna a ação de voar"""
        return f"{self.__nome} está voando"

    def granir(self) ->str:
        """Retorna o som emitido"""
        return "Quack! Quack!"