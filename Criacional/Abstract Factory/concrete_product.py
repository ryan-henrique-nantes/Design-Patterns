"""Classes Concreta para ser usadas no Abstract Factory"""
from abstract_product import *

class Funcionario(IFuncionario):
    """Classe Concreta de Funcionario"""
    def __init__(self):
        self.__codigo = None
        self.__idade: None
        self.__nome: None

    @classmethod 
    def new(cls: "Funcionario") -> IFuncionario:
        """Implementação do Método de Fabricação"""
        return cls()

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
        """Metódo de Dormir"""
        print(self.__nome + " esta dormindo!")

    def __calcular_tarifa(self): ...

class Marca(IMarca):  
    """Classe Concreta de Marca"""

    def __init__(self):
        self.__cnpj = None
        self.__lista_funcionario = []
        self.__nome = None

    @classmethod
    def new(cls: "Marca") -> IMarca:
        """Implementação do Método de Fabricação"""
        return cls()

    @property
    def cnpj(self) -> str:
        """Property do CNPJ """
        return self.__cnpj

    @property
    def lista_funcionario(self) -> list:
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

    def remover_functionario(self, codigo: int) -> IMarca:
        """Metódo de Remover Funcionario pelo ID"""
        for funcionario in self.__lista_funcionario:
            if funcionario.codigo == codigo:
                self.__lista_funcionario.remove(funcionario)
        return self

    def funcionario(self, codigo: int) -> IFuncionario:
        """Metódo de Pegar Funcionario"""
        for funcionario in self.__lista_funcionario:
            if funcionario.codigo == codigo:
                return funcionario
        return None

class Produto(IProduto):
    """Classe concreta de Produto"""

    def __init__(self) -> None:
        self.__descricao = None
        self.__marca = None
        self.__preco = None

    @classmethod
    def new(cls: "Produto") -> IProduto:
        """Implementação do Método de Fabricação"""
        return cls()

    @property
    def descricao(self) -> str:
        """Getter de descrição"""
        return self.__descricao

    @property
    def marca(self) -> IMarca:
        """Getter da marca"""
        return self.__marca

    @property
    def preco(self) -> float:
        """Getter do preço"""
        return self.__preco

    def set_descricao(self, value: str) -> IProduto:
        """Setter de descrição, usando fluent"""
        self.__descricao = value
        return self

    def set_marca(self, value: IMarca) -> IProduto:
        """Setter da marca, usando fluent"""
        self.__marca = value
        return self

    def set_preco(self, value: float) -> IProduto:
        """Setter do preço, usando fluent"""
        self.__preco = value
        return self