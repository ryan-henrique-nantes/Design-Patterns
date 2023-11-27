"""Module do Concrete Component do padrão Decorator."""
from interface_component import IMensagem

class Mensagem(IMensagem):
    """Classe Concrete Component do padrão Decorator."""

    def __init__(self: "Mensagem", conteudo: str) -> None:
        """Método construtor."""
        self._conteudo = conteudo

    @classmethod
    def new(cls: "Mensagem", conteudo: str) -> IMensagem:
        """Método que retorna uma instância da classe Mensagem."""
        return cls(conteudo)

    def enviar(self: "Mensagem") -> None:
        """Método que envia a mensagem."""
        return self._conteudo