"""Module da classe Concreta do Abstract Factory"""
from abstract_factory import *
from concrete_product import *

class Factory(IFactory):
    """Classe Concreta de Factory"""

    def __init__(self) -> None:
        """Construtor da Classe Concreta"""
        self.__funcionario = None
        self.__marca = None
        self.__produto = None

    @classmethod
    def new(cls: "Factory") -> IFactory:
        """Implementação do Método de Fabricação"""
        return cls()

    @property
    def funcionario(self) -> IFuncionario:
        """Metódo de Criar Funcionario"""
        if self.__funcionario is None:
            self.__funcionario = Funcionario.new()
        return self.__funcionario

    @property
    def marca(self) -> IMarca:
        """Metódo de Criar Marca"""
        if self.__marca is None:
            self.__marca = Marca.new()
        return self.__marca

    @property
    def produto(self) -> IProduto:
        """Metódo de Criar Produto"""
        if self.__produto is None:
            self.__produto = Produto.new()
        return self.__produto