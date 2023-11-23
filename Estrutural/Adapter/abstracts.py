"""Module de classes target e adaptee"""
from abc import *

class IPassaro(ABC):
    """Interface que define o comportamento de um pássaro"""

    @abstractmethod
    def voar(self) ->str: ...
    """Método que retorna a ação de voar"""

    @abstractmethod
    def granir(self) ->str: ...
    """Método que retorna o som emitido"""

class IPassaroBrinquedo(ABC):
    """Interface que define o comportamento de um pato de borracha"""

    @abstractmethod
    def apertar(self) ->str: ...
    """Método que retorna a ação de apertar"""