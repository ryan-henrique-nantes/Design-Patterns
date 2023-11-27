"""Module do Concrete Decorator do padrão Decorator."""
from interface_decorator import Decorator
from datetime import datetime

class DataHoraMensagem(Decorator):
    """Classe Concrete Decorator do padrão Decorator."""

    def __init__(self: "DataHoraMensagem", mensagem: Decorator) -> None:
        """Método construtor."""
        super().__init__(mensagem)

    @classmethod
    def new(cls: "DataHoraMensagem", mensagem: Decorator) -> Decorator:
        """Método que retorna uma instância da classe DataHoraMensagem."""
        return cls(mensagem)

    def enviar(self: "DataHoraMensagem") -> None:
        """Método que envia a mensagem."""
        return f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} - {self._mensagem.enviar()}'
