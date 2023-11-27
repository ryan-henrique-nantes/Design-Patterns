"""Module do Decorator do padrão Decorator."""
from interface_component import IMensagem

class Decorator(IMensagem):
    """Classe abstrata do Decorator do padrão Decorator."""

    def __init__(self: "Decorator", mensagem: IMensagem) -> None:
        """Método construtor."""
        self._mensagem = mensagem

    @classmethod
    def new(cls: "Decorator", mensagem: IMensagem) -> IMensagem:
        """Método que retorna uma instância da classe Decorator."""
        return cls(mensagem)

    def enviar(self: "Decorator") -> None:
        """Método que envia a mensagem."""
        return self._mensagem.enviar() + '\n\n'