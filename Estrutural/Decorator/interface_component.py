"""Module do Component Interface do padrão Decorator."""

class IMensagem:
    """Classe abstrata do Component do padrão Decorator."""

    def enviar(self) -> None: ...
    """Método Operation da classe Component."""
    