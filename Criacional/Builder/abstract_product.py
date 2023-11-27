"""Module da classe abstrata de produto."""

class IFuncionario:
    """classe abstrata de produto."""

    @property
    def nome(self) -> str: ...
    """Método abstrato de retorno do nome."""

    @property
    def idade(self) -> int: ...
    """Método abstrato de retorno da idade."""

    @property
    def cidade(self) -> str: ...
    """Método abstrato de retorno da cidade."""

    @property
    def estado(self) -> str: ...
    """Método abstrato de retorno do estado."""

    def set_nome(self, nome: str) -> "IFuncionario": ...
    """Método abstrato de atribuição do nome."""

    def set_idade(self, idade: int) -> "IFuncionario": ...
    """Método abstrato de atribuição da idade."""

    def set_cidade(self, cidade: str) -> "IFuncionario": ...
    """Método abstrato de atribuição da cidade."""

    def set_estado(self, estado: str) -> "IFuncionario": ...
    """Método abstrato de atribuição do estado."""