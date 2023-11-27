"""Module de classes target e adaptee"""

class IPassaro:
    """Interface que define o comportamento de um pássaro"""

    def voar(self) ->str: ...
    """Método que retorna a ação de voar"""

    def granir(self) ->str: ...
    """Método que retorna o som emitido"""

class IPassaroBrinquedo:
    """Interface que define o comportamento de um pato de borracha"""

    def apertar(self) ->str: ...
    """Método que retorna a ação de apertar"""