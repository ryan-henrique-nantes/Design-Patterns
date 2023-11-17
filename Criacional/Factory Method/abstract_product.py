"""Module de Produto Abstrato do Design Pattern: Factory Method"""
from abc import *

class IGuitarra(ABC):
    """Classe Abstrata de produto Guitarra"""
    def __init__(self): ...

    @abstractmethod
    def marca(self) -> str: ...
    """Metodo Marca a ser implementada"""

    @abstractmethod
    def ano_fabricacao(self) -> int: ...
    """Metodo Ano de Fabricação a ser implementada"""

    @abstractmethod
    def modelo(self) -> list[str]: ...
    """Metodo Modelo de Guitarra a ser implementada"""