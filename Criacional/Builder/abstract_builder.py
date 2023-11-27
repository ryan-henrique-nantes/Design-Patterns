"""Module da classe abstrata do padrão Builder."""

class IBuilder:
    """Classe abstrata do padrão Builder."""

    def builder_cabecalho(self) -> "IBuilder": ...
    """Método abstrato de construção do cabeçalho."""

    def builder_corpo(self) -> "IBuilder": ...
    """Método abstrato de construção do corpo."""

    def save(self) -> "IBuilder": ...
    """Método abstrato de salvamento do relatório."""

    def get_relatorio(self) -> str: ...
    """Método abstrato de retorno do relatório."""