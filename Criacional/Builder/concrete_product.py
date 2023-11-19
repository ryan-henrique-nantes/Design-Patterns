"""Module da classe concreta do produto."""
from abstract_product import *

class Funcionario(IFuncionario):
    """Classe concreta de produto."""

    def __init__(self) -> None:
        """Construtor da classe."""
        self.__nome = None
        self.__idade = None
        self.__cidade = None
        self.__estado = None

    @classmethod
    def new(cls: "Funcionario") -> IFuncionario:
        """Implementação do Método de Fabricação."""
        return cls()

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def idade(self) -> int:
        return self.__idade

    @property
    def cidade(self) -> str:
        return self.__cidade

    @property
    def estado(self) -> str:
        return self.__estado

    def set_nome(self, nome: str) -> IFuncionario:
        self.__nome = nome
        return self

    def set_cidade(self, cidade: str) -> IFuncionario:
        self.__cidade = cidade
        return self

    def set_estado(self, estado: str) -> IFuncionario:
        self.__estado = estado
        return self

    def set_idade(self, idade: int) -> IFuncionario:
        self.__idade = idade
        return self