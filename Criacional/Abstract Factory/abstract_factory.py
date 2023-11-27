"""Module da Classe Abstrata de Factory do Abstract Factory"""
from abstract_product import *

class IFactory:
    """Classe Abstrata de Factory"""

    @property
    def funcionario(self) -> IFuncionario: ...
    """Metódo Abstrato de Criar Funcionario"""

    @property
    def marca(self) -> IMarca: ...
    """Metódo Abstrato de Criar Marca"""

    @property
    def produto(self) -> IProduto: ...
    """Metódo Abstrato de Criar Produto"""