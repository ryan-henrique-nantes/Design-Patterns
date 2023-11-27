"""Classes Abstratas para ser usadas no Abstract Factory"""

class IFuncionario:
    """Classe Abstrata de Funcionario"""

    @property 
    def codigo(self) -> int: ...
    """Property de Codigo"""

    @property 
    def idade(self) -> int: ...
    """Property de Idade"""

    @property 
    def nome(self) -> str: ...
    """Property de Nome"""

    def set_codigo(self, value: int) -> "IFuncionario": ...
    """Setter do Codigo"""

    def set_idade(self, value: int) -> "IFuncionario": ...
    """Setter da Idade"""

    def set_nome(self, value: str) -> "IFuncionario": ...
    """Setter do Nome"""

    def dormir(self) -> None: ...
    """Metódo Abstrato de Dormir"""

class IMarca:  
    """Classe Abstrata de Marca"""

    @property 
    def cnpj(self) -> str: ...
    """Property do CNPJ """

    @property
    def lista_funcionario(self) -> list: ...
    """Property da Lista de Funcionarios"""

    @property 
    def nome(self) -> str: ...
    """Property do Nome da Empresa"""

    def set_nome(self, value: str) -> "IMarca": ...
    """Setter do Nome"""

    def set_cnpj(self, value: str) -> "IMarca": ...
    """Setter do Cnpj"""

    def adicionar_funcionario(self, funcionario: IFuncionario) -> "IMarca": ...
    """Metódo de Adicionar Funcionario"""

    def remover_functionario(self, codigo: int) -> "IMarca": ...
    """Metódo de Remover Funcionario pelo ID"""

    def funcionario(self, codigo: int) -> IFuncionario: ...
    """Metódo de Pegar Funcionario"""

class IProduto:
    """Classe abstrata de Produto"""

    @property 
    def descricao(self) -> str: ...
    """Getter abstrato de descrição"""

    @property
    def marca(self) -> IMarca: ...
    """Getter abstrato da marca"""

    @property 
    def preco(self) -> float: ...
    """Getter abstrato do preço"""

    def set_descricao(self, value: str) -> "IProduto": ...
    """Setter abstrato de descrição, usando fluent"""

    def set_marca(self, value: IMarca) -> "IProduto": ...
    """Setter abstrato da marca, usando fluent"""

    def set_preco(self, value: float) -> "IProduto": ...
    """Setter abstrato do preço, usando fluent"""