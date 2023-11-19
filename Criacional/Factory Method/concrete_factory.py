"""Module da classe Concreta do Factory Method"""
from typing import Any
from abstract_factory import *
from abstract_product import *
from concretes_product import *

class Factory(IFactory):
    """Classe Concreta do Factory Method"""

    @classmethod
    def new(cls: "Factory") -> IFactory:
        """Implementação do Método de Fabricação"""
        return cls()

    def guitarra(self, opcao: Tipo) -> IGuitarra:
        """Implementação do metodo guitarra"""
        if opcao ==  Tipo.FENDER_STRATOCASTER:
            return FenderStratocaster.new()
        elif opcao == Tipo.FENDER_TELECASTER:
            return FenderTelecaster.new()
        elif opcao == Tipo.GIBSON_LES_PAUL:
            return GibsonLesPaul.new()
        elif opcao == Tipo.GIBSON_SG:
            return GibsonSG.new()
    