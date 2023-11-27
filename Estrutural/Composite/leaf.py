"""Module do Leaf do padrão Composite."""
"""Module do Leaf do padrão Composite."""
import random
from component_interface import IViagem

class Viagem(IViagem):
    """Classe Leaf do padrão Composite."""

    @classmethod
    def new(cls: "Viagem") -> IViagem:
        """Método que retorna uma instância da classe Viagem."""
        return cls()

    def calcular_valor(self) -> float:
        """Método que retorna o valor da viagem."""
        return random.randint(1, 100)

