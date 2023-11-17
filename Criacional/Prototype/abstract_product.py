"""Module da classe abstrata do Produto que Herda da IPrototype"""
from abstract_prototype import *

class IProduto(IPrototype):
    """Classe abstrata de Produto"""

    @abstractmethod
    def get_descricao(self) -> str: ...
    """Getter abstrato de descrição"""

    @abstractmethod
    def set_descricao(self, value: str) -> "IProduto": ...
    """Setter abstrato de descrição, usando fluent"""

    @abstractmethod
    def get_marca(self) -> str: ...
    """Getter abstrato da marca"""

    @abstractmethod
    def set_marca(self, value: str) -> "IProduto": ...
    """Setter abstrato da marca, usando fluent"""

    @abstractmethod
    def get_preco(self) -> float: ...
    """Getter abstrato do preço"""

    @abstractmethod
    def set_preco(self, value: float) -> "IProduto": ...
    """Setter abstrato do preço, usando fluent"""
