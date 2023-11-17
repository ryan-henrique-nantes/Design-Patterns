"""Module da classe Abstrata do Prototype"""
from abc import *

class IPrototype(ABC):
    """Classe Abstrata de Prototype"""

    def __init__(self): ...

    @abstractmethod
    def clone(self) -> "IPrototype":...
    """Função Clone do Prototype"""