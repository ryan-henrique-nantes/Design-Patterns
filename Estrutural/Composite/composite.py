"""Module do Composite do padrão Composite."""
from component_interface import IViagem

class PacoteViagem(IViagem):
    """Classe Composite do padrão Composite."""

    def __init__(self) -> None:
        self.__viagens = []

    def adicionar_viagem(self, viagem: IViagem) -> None:
        """Método que adiciona uma viagem."""
        self.__viagens.append(viagem)

    def calcular_valor(self) -> float:
        """Método que retorna o valor da viagem."""
        valor = 0
        for viagem in self.__viagens:
            valor += viagem.calcular_valor()
        return valor

    