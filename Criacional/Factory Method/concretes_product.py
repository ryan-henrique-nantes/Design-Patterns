"""Module das Classes Concreta do Factory Method"""
from abstract_product import *

class GibsonLesPaul(IGuitarra):
    """Implementação do IGuitarra"""

    def marca(self) -> str:
        """Implementação da Marca"""
        return "Les Paul"
    
    def ano_fabricacao(self) -> int:
        """Implementação do Ano de Fabricação"""
        return 2012
    
    def modelo(self) -> list[str]:
        """Implementação dos modelos"""
        return ["dourado", "preto", "vermelho"]

class GibsonSG(IGuitarra):
    """Implementação do IGuitarra"""

    def marca(self) -> str:
        """Implementação da Marca"""
        return "SG"
    
    def ano_fabricacao(self) -> int:
        """Implementação do Ano de Fabricação"""
        return 2016
    
    def modelo(self) -> list[str]:
        """Implementação dos modelos"""
        return ["branco", "preto"]

class FenderStratocaster(IGuitarra):
    """Implementação do IGuitarra"""

    def marca(self) -> str:
        """Implementação da Marca"""
        return "Stratocaster"
    
    def ano_fabricacao(self) -> int:
        """Implementação do Ano de Fabricação"""
        return 2001
    
    def modelo(self) -> list[str]:
        """Implementação dos modelos"""
        return ["carmesin", "marrom"]
    
class FenderTelecaster(IGuitarra):
    """Implementação do IGuitarra"""

    def marca(self) -> str:
        """Implementação da Marca"""
        return "Telecaster"
    
    def ano_fabricacao(self) -> int:
        """Implementação do Ano de Fabricação"""
        return 2020
    
    def modelo(self) -> list[str]:
        """Implementação dos modelos"""
        return ["azul", "cobre"]