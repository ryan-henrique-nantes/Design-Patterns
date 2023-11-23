"""Module da classe Adapter que vai adaptar a classe adaptee para a classe target"""
from abstracts import IPassaro, IPassaroBrinquedo
from target import Pato

class PatoDeBorrachaAdapter(IPassaro):
    """Classe que representa um pato de borracha"""
    def __init__(self, pato_de_borracha:IPassaroBrinquedo):
        """Cria um novo pato de borracha"""
        self.__pato_de_borracha = pato_de_borracha

    @classmethod
    def new(cls, pato_de_borracha:IPassaroBrinquedo) -> IPassaro:
        """Cria um novo pato de borracha"""
        return cls(pato_de_borracha)
        
    def voar(self) ->str:
        """Retorna a ação de voar"""
        return "Pato de borracha não voa"

    def granir(self) ->str:
        """Retorna o som emitido"""
        return self.__pato_de_borracha.apertar()