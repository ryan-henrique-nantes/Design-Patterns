"""Classes Concreta para ser usadas no Abstract Factory"""
from abstract_products import *

class Funcionario(IFuncionario):
    """Classe Concreta de Funcionario"""
    def __init__(self):
        self.__codigo = None
        self.__idade: None
        self.__nome: None

    @property
    def codigo(self) -> int:
        """Property de Codigo"""    
        return self.__codigo

    @property
    def idade(self) -> int:
        """Property de Idade"""
        return self.__idade

    @property
    def nome(self) -> str:
        """Property de Nome"""
        return self.__nome
    
    def set_codigo(self, value: int) -> IFuncionario:
        """Setter do Codigo"""
        self.__codigo = value
        return self
    
    def set_idade(self, value: int) -> IFuncionario:
        """Setter da Idade"""
        self.__idade = value
        return self

    def set_nome(self, value: str) -> IFuncionario:
        """Setter do Nome"""
        self.__nome = value
        return self
    
    def dormir(self) -> None:
        """Metódo Abstrato de Dormir"""
        print("dormindo!")

class Marca(IMarca):  
    """Classe Concreta de Marca"""

    def __init__(self):
        self.__cnpj = None
        self.__lista_funcionario = []
        self.__nome = None

    @property
    def cnpj(self) -> str:
        """Property do CNPJ """
        return self.__cnpj

    @property
    def lista_funcionario(self) -> list[IFuncionario]:
        """Property da Lista de Funcionarios"""
        return self.__lista_funcionario
    
    @property
    def nome(self) -> str:
        """Property do Nome da Empresa"""
        return self.__nome

    def set_nome(self, value: str) -> IMarca:
        """Setter do Nome"""
        self.__nome = value
        return self

    def set_cnpj(self, value: str) -> IMarca:
        """Setter do Cnpj"""
        self.__cnpj = value
        return self
    
    def adicionar_funcionario(self, funcionario: IFuncionario) -> IMarca:
        """Metódo de Adicionar Funcionario"""
        self.__lista_funcionario.append(funcionario)
        return self

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