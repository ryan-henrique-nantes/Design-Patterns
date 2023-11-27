"""Module da Classe Abstrata do Factory Method"""
from enum import Enum
from abstract_product import IGuitarra

class Tipo(Enum):
    """Opções da Factory"""
    GIBSON_LES_PAUL = 0
    GIBSON_SG = 1
    FENDER_STRATOCASTER = 2
    FENDER_TELECASTER = 3

class IFactory:
    """Classe Abstrata do Factory"""

    def guitarra(self, opcao: Tipo) -> IGuitarra: ...
    """Metodo Abstrato de Obter Guitarra"""