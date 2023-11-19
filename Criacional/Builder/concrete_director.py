""""Module da classe concreta do Director do padrão Builder."""
from concrete_builder import *
from abstract_product import *
from abstract_director import *

class Director(IDirector):
    """Classe concreta do Director."""

    @classmethod
    def new(cls: "Director") -> IDirector:
        """Método de inicialização do Director."""
        return cls()

    def build(self, elemento: IFuncionario) -> list:
        """Método de construção do relatório."""
        return BuilderCSV.new(elemento).builder_cabecalho().builder_corpo().save().get_relatorio()