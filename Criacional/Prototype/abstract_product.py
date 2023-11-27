"""Module da classe abstrata do Produto que Herda da IPrototype"""
from abstract_prototype import *

class IProduto(IPrototype):
    """Classe abstrata de Produto"""

    def get_descricao(self) -> str: ...
    """Getter abstrato de descrição"""

    def set_descricao(self, value: str) -> "IProduto": ...
    """Setter abstrato de descrição, usando fluent"""

    def get_marca(self) -> str: ...
    """Getter abstrato da marca"""

    def set_marca(self, value: str) -> "IProduto": ...
    """Setter abstrato da marca, usando fluent"""

    def get_preco(self) -> float: ...
    """Getter abstrato do preço"""

    def set_preco(self, value: float) -> "IProduto": ...
    """Setter abstrato do preço, usando fluent"""
