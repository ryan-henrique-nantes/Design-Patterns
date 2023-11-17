"""Module da classe concreta do Produto, implementando toda a lógica do Prototype"""
from abstract_product import *

class Produto(IProduto):
    """Classe concreta do IProduto"""
    def __init__(self)-> None:
        self.__descricao = None
        self.__marca = None
        self.__preco = None

    def set_descricao(self, value: str) -> IProduto:
        """Setter da descrição do produto, usando fluent"""
        self.__descricao = value
        return self

    def set_marca(self, value: str) -> IProduto:
        """Setter da marca do produto, usando fluent"""
        self.__marca = value
        return self

    def set_preco(self, value: float) -> IProduto:
        """Setter do preço do produto, usando fluent"""
        self.__preco = value
        return self
    
    def get_descricao(self) -> str:
        """Getter da descrição do produto"""
        return self.__descricao
    
    def get_marca(self) -> str:
        """Getter da marca do produto"""
        return self.__marca
    
    def get_preco(self) -> float:
        """Getter do preço do produto"""
        return self.__preco
    
    def clone(self):
        """Metódo de clonar do Prototype"""
        return Produto().set_descricao(self.__descricao).set_marca(self.__marca).set_preco(self.__preco)