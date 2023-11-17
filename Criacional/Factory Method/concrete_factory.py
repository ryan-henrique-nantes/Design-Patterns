"""Module da classe Concreta do Factory Method"""
from abstract_factory import *
from abstract_product import *
from concretes_product import *

class Factory(IFactory):
    """Classe Concreta do Factory Method"""
    def guitarra(self, opcao: Tipo) -> IGuitarra:
        """Implementação do metodo guitarra"""
        match opcao:
            case Tipo.FENDER_STRATOCASTER:
                return FenderStratocaster()
            case Tipo.FENDER_TELECASTER:
                return FenderTelecaster()
            case Tipo.GIBSON_LES_PAUL:
                return GibsonLesPaul()
            case Tipo.GIBSON_SG:
                return GibsonSG()
    