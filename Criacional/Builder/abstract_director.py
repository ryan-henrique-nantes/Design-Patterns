"""Module da classe abstrata director do padrão Builder."""
from abstract_product import *

class IDirector:
    """Classe abstrata do Director."""

    def build(self, elemento: IFuncionario) -> list: ...
    """Método de construção do relatório."""
