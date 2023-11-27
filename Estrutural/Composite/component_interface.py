"""Module do Component Interface e Operation do padrão Composite."""

class IViagem:
    """Classe abstrata do Component do padrão Composite."""

    def calcular_valor(self) -> float: ...
    """Método Operation da classe Component."""