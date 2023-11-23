"""Module da classe adaptee que vai ser adaptada"""
from abstracts import IPassaroBrinquedo

class PatoDeBorracha(IPassaroBrinquedo):
    """Classe que representa um pato de borracha"""
    def __init__(self, nome:str):
        """Cria um novo pato de borracha"""
        self.__nome = nome

    @classmethod
    def new(cls, nome:str) -> IPassaroBrinquedo:
        """Cria um novo pato de borracha"""
        return cls(nome)

    def apertar(self) ->str:
        """Retorna a ação de apertar"""
        return "Squeak! Squeak!"