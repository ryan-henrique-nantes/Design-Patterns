"""Module do Implementor do padrão Bridge."""

class IVeiculo:
    """Interface que define o comportamento do implementor."""

    def ligar(self): ...
    """Método que retorna a ação de ligar."""

    def desligar(self): ...
    """Método que retorna a ação de desligar."""

    def verificar_ligado(self) -> bool: ...
    """Método que verifica se esta ligado."""
    
    @property
    def velocidade(self) -> int: ...
    """Método que retorna o valor de velocidade."""

    @velocidade.setter
    def velocidade(self, velocidade: int): ...
    """Método que retorna a ação de mudar a velocidade."""

    @property
    def direcao(self) -> str: ...
    """Método que retorna o valor de direção."""

    @direcao.setter
    def direcao(self, direcao: str): ...
    """Método que retorna a ação de mudar a direção."""
