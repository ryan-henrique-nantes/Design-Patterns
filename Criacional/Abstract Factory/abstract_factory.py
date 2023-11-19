"""Module da Classe Abstrata de Factory do Abstract Factory"""
from abc import *
from abstract_product import *

class IFactory(ABC):
    """Classe Abstrata de Factory"""

    @property
    @abstractmethod
    def funcionario(self) -> IFuncionario: ...
    """Metódo Abstrato de Criar Funcionario"""

    @property
    @abstractmethod
    def marca(self) -> IMarca: ...
    """Metódo Abstrato de Criar Marca"""

    @property
    @abstractmethod
    def produto(self) -> IProduto: ...
    """Metódo Abstrato de Criar Produto"""