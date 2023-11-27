"""Module de Produto Abstrato do Design Pattern: Factory Method"""

class IGuitarras:
    """Classe Abstrata de produto Guitarra"""

    def marca(self) -> str: ...
    """Metodo Marca a ser implementada"""

    def ano_fabricacao(self) -> int: ...
    """Metodo Ano de Fabricação a ser implementada"""

    def modelo(self) -> list: ...
    """Metodo Modelo de Guitarra a ser implementada"""