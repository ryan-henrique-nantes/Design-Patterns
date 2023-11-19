"""Module da classe abstrata de produto."""
from abc import *

class IFuncionario(ABC):
    """classe abstrata de produto."""

    @property
    @abstractmethod
    def nome(self) -> str: ...
    """Método abstrato de retorno do nome."""

    @property
    @abstractmethod
    def idade(self) -> int: ...
    """Método abstrato de retorno da idade."""

    @property
    @abstractmethod
    def cidade(self) -> str: ...
    """Método abstrato de retorno da cidade."""

    @property
    @abstractmethod
    def estado(self) -> str: ...
    """Método abstrato de retorno do estado."""

    @abstractmethod
    def set_nome(self, nome: str) -> "IFuncionario": ...
    """Método abstrato de atribuição do nome."""

    @abstractmethod
    def set_idade(self, idade: int) -> "IFuncionario": ...
    """Método abstrato de atribuição da idade."""

    @abstractmethod
    def set_cidade(self, cidade: str) -> "IFuncionario": ...
    """Método abstrato de atribuição da cidade."""

    @abstractmethod
    def set_estado(self, estado: str) -> "IFuncionario": ...
    """Método abstrato de atribuição do estado."""