"""Module do Refined Abstraction do padrão Bridge."""
from abstraction_interface import IPiloto
from implementor_interface import IVeiculo

class Piloto(IPiloto):
    """Classe que implementa o comportamento do Refined Abstraction."""

    def __init__(self, veiculo: IVeiculo) -> None:
        """Cria uma instância da classe Piloto."""
        self.__veiculo = veiculo

    @classmethod
    def new(cls: "Piloto", veiculo: IVeiculo) -> IPiloto:
        """Método que retorna uma instância da classe Piloto."""
        return cls(veiculo)

    def toggle_ligar(self):
        """Método que retorna a ação de ligar."""
        if self.__veiculo.verificar_ligado():
            self.__veiculo.desligar()
            print('Veículo está desligado.')
            exit()
        self.__veiculo.ligar()
        print('Veículo está ligado.')

    def aumentar_velocidade(self):
        """Método que retorna a ação de aumentar a velocidade."""
        self.__veiculo.velocidade += 1
        print(f'Velocidade atual: {self.__veiculo.velocidade}')

    def diminuir_velocidade(self):
        """Método que retorna a ação de diminuir a velocidade."""
        self.__veiculo.velocidade -= 1
        print(f'Velocidade atual: {self.__veiculo.velocidade}')

    def virar_a_direita(self):
        """Método que retorna a ação de virar a direita."""
        self.__veiculo.direcao = 'Leste'
        print(f'Direção atual: {self.__veiculo.direcao}')

    def virar_a_esquerda(self):
        """Método que retorna a ação de virar a esquerda."""
        self.__veiculo.direcao = 'Oeste'
        print(f'Direção atual: {self.__veiculo.direcao}')

    def dar_re(self):
        """Método que retorna a ação de dar re."""
        self.__veiculo.direcao = 'Sul'
        print(f'Direção atual: {self.__veiculo.direcao}')

    def freiar(self):
        """Método que retorna a ação de freiar."""
        self.__veiculo.velocidade = 0
        print(f'Velocidade atual: {self.__veiculo.velocidade}')