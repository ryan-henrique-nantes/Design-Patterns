"""Classes Abstratas para ser usadas no Abstract Factory"""
from abc import *

class IFuncionario(ABC):
    """Classe Abstrata de Funcionario"""
    @property @abstractmethod 
    def codigo(self) -> int: ...
    """Property de Codigo"""

    @property @abstractmethod
    def idade(self) -> int: ...
    """Property de Idade"""

    @property @abstractmethod
    def nome(self) -> str: ...
    """Property de Nome"""

    @abstractmethod
    def set_codigo(self, value: int) -> "IFuncionario": ...
    """Setter do Codigo"""

    @abstractmethod
    def set_idade(self, value: int) -> "IFuncionario": ...
    """Setter da Idade"""

    @abstractmethod
    def set_nome(self, value: str) -> "IFuncionario": ...
    """Setter do Nome"""

    @abstractmethod
    def dormir(self) -> None: ...
    """Metódo Abstrato de Dormir"""

class IMarca(ABC):  
    """Classe Abstrata de Marca"""

    @property @abstractmethod
    def cnpj(self) -> str: ...
    """Property do CNPJ """

    @property @abstractmethod
    def lista_funcionario(self) -> list[IFuncionario]: ...
    """Property da Lista de Funcionarios"""

    @property @abstractmethod
    def nome(self) -> str: ...
    """Property do Nome da Empresa"""

    @abstractmethod
    def set_nome(self, value: str) -> "IMarca": ...
    """Setter do Nome"""

    @abstractmethod
    def set_cnpj(self, value: str) -> "IMarca": ...
    """Setter do Cnpj"""

    @abstractmethod
    def adicionar_funcionario(self, funcionario: IFuncionario) -> "IMarca": ...
    """Metódo de Adicionar Funcionario"""

    @abstractmethod
    def remover_functionario(self, codigo: int) -> "IMarca": ...
    """Metódo de Remover Funcionario pelo ID"""

    @abstractmethod
    def funcionario(self, codigo: int) -> IFuncionario: ...
    """Metódo de Pegar Funcionario"""

class IProduto(ABC):
    """Classe abstrata de Produto"""

    @property @abstractmethod
    def descricao(self) -> str: ...
    """Getter abstrato de descrição"""

    @property @abstractmethod
    def marca(self) -> IMarca: ...
    """Getter abstrato da marca"""

    @property @abstractmethod
    def preco(self) -> float: ...
    """Getter abstrato do preço"""

    @abstractmethod
    def set_descricao(self, value: str) -> "IProduto": ...
    """Setter abstrato de descrição, usando fluent"""

    @abstractmethod
    def set_marca(self, value: IMarca) -> "IProduto": ...
    """Setter abstrato da marca, usando fluent"""

    @abstractmethod
    def set_preco(self, value: float) -> "IProduto": ...
    """Setter abstrato do preço, usando fluent"""