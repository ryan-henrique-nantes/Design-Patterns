"""Module da classe abstrata director do padrão Builder."""
from abc import *
from abstract_product import *

class IDirector(ABC):
    """Classe abstrata do Director."""

    @abstractmethod
    def build(self, elemento: IFuncionario) -> list: ...
    """Método de construção do relatório."""
