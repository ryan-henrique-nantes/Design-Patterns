"""Module do Implementor Concrete do padrão Bridge."""
from implementor_interface import IVeiculo

class Veiculo(IVeiculo):
    """Classe base que implementa o comportamento do implementor."""

    def __init__(self):
        """Cria uma instância da classe Veiculo."""
        self.__ligado = False
        self.__velocidade = 0
        self.__direcao = 'Norte'

    def ligar(self):
        """Método que retorna a ação de ligar."""
        self.__ligado = True

    def desligar(self):
        """Método que retorna a ação de desligar."""
        self.__ligado = False

    def verificar_ligado(self) -> bool:
        """Método que verifica se esta ligado."""
        return self.__ligado

    @property
    def velocidade(self) -> int:
        """Método que retorna o valor de velocidade."""
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, velocidade: int):
        """Método que retorna a ação de mudar a velocidade."""
        self.__velocidade = velocidade

    @property
    def direcao(self) -> str:
        """Método que retorna o valor de direção."""
        return self.__direcao

    @direcao.setter
    def direcao(self, direcao: str):
        """Método que retorna a ação de mudar a direção."""
        self.__direcao = direcao

class Carro(Veiculo):
    """Classe que implementa o comportamento do implementor."""

    def __init__(self):
        super().__init__()

    @classmethod
    def new(cls: "Carro") -> IVeiculo:
        """Método que retorna uma instância da classe Carro."""
        return cls()

    def ligar(self):
        """Método que retorna a ação de ligar."""
        super().ligar()
        print('Carro está ligado.')

    def desligar(self):
        """Método que retorna a ação de desligar."""
        super().desligar()
        print('Carro está desligado.')

    @Veiculo.velocidade.setter
    def velocidade(self, velocidade: int):
        """Método que retorna a ação de mudar a velocidade."""
        Veiculo.velocidade.fset(self, velocidade)
        print(f'Carro está a {self.velocidade} km/h.')

    @Veiculo.direcao.setter
    def direcao(self, direcao: str):
        """Método que retorna a ação de mudar a direção."""
        Veiculo.direcao.fset(self, direcao)
        print(f'Carro está indo para {self.direcao}.')

class Moto(Veiculo):
    """Classe que implementa o comportamento do implementor."""

    def __init__(self):
        super().__init__()

    @classmethod
    def new(cls: "Moto") -> IVeiculo:
        """Método que retorna uma instância da classe Moto."""
        return cls()

    def ligar(self):
        """Método que retorna a ação de ligar."""
        super().ligar()
        print('Moto está ligada.')

    def desligar(self):
        """Método que retorna a ação de desligar."""
        super().desligar()
        print('Moto está desligada.')

    @Veiculo.velocidade.setter
    def velocidade(self, velocidade: int):
        """Método que retorna a ação de mudar a velocidade."""
        Veiculo.velocidade.fset(self, velocidade)
        print(f'Moto está a {self.velocidade} km/h.')

    @Veiculo.direcao.setter
    def direcao(self, direcao: str):
        """Método que retorna a ação de mudar a direção."""
        Veiculo.direcao.fset(self, direcao)
        print(f'Moto está indo para {self.direcao}.')

class Caminhao(Veiculo):
    """Classe que implementa o comportamento do implementor."""

    def __init__(self):
        super().__init__()

    @classmethod
    def new(cls: "Caminhao") -> IVeiculo:
        """Método que retorna uma instância da classe Caminhao."""
        return cls()

    def ligar(self):
        """Método que retorna a ação de ligar."""
        super().ligar()
        print('Caminhão está ligado.')

    def desligar(self):
        """Método que retorna a ação de desligar."""
        super().desligar()
        print('Caminhão está desligado.')

    @Veiculo.velocidade.setter
    def velocidade(self, velocidade: int):
        """Método que retorna a ação de mudar a velocidade."""
        Veiculo.velocidade.fset(self, velocidade)
        print(f'Caminhão está a {self.velocidade} km/h.')

    @Veiculo.direcao.setter
    def direcao(self, direcao: str):
        """Método que retorna a ação de mudar a direção."""
        Veiculo.direcao.fset(self, direcao)
        print(f'Caminhão está indo para {self.direcao}.')