"""Module da classe Abstrata do Prototype"""

class IPrototype:
    """Classe Abstrata de Prototype"""

    def clone(self) -> "IPrototype":...
    """Função Clone do Prototype"""