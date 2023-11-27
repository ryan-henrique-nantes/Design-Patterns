"""Module do Abstraction Interface do padrão Bridge."""

class IPiloto:
    """Classe abstrata que define a interface do Abstraction."""

    def toggle_ligar(self): ...
    """Método que retorna a ação de ligar."""

    def aumentar_velocidade(self): ...
    """Método que retorna a ação de aumentar a velocidade."""

    def diminuir_velocidade(self): ...
    """Método que retorna a ação de diminuir a velocidade."""

    def virar_a_direita(self): ...
    """Método que retorna a ação de virar a direita."""

    def virar_a_esquerda(self): ...
    """Método que retorna a ação de virar a esquerda."""

    def dar_re(self): ...
    """Método que retorna a ação de dar re."""

    def freiar(self): ...
    """Método que retorna a ação de freiar."""