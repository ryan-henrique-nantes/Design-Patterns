"""Module da classe abstrata do padrão Builder."""
from abc import *

class IBuilder(ABC):
    """Classe abstrata do padrão Builder."""

    @abstractmethod
    def builder_cabecalho(self) -> "IBuilder": ...
    """Método abstrato de construção do cabeçalho."""

    @abstractmethod
    def builder_corpo(self) -> "IBuilder": ...
    """Método abstrato de construção do corpo."""

    @abstractmethod
    def save(self) -> "IBuilder": ...
    """Método abstrato de salvamento do relatório."""

    @abstractmethod
    def get_relatorio(self) -> str: ...
    """Método abstrato de retorno do relatório."""