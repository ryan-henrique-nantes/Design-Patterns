"""Module da classe concreta do padrão Builder."""
from abstract_builder import *
from abstract_product import *
import csv

class BuilderCSV(IBuilder):
    """Classe concreta do padrão Builder."""

    def __init__(self, elemento: IFuncionario) -> None:
        self.__relatorio = []
        self.__elemento = elemento
        self.ARQUIVO = "funcionarios.csv"
    @classmethod
    def new(cls: "BuilderCSV", elemento: IFuncionario) -> IBuilder:
        """Implementação do Método de Fabricação."""
        return cls(elemento)
        
    def builder_cabecalho(self) -> IBuilder:
        """Método de construção do cabeçalho."""
        self.__relatorio.append(["Nome; Idade; Cidade; Estado"])
        return self

    def builder_corpo(self) -> IBuilder:
        """Método de construção do corpo."""
        self.__relatorio.append([self.__elemento.nome + "; " + str(self.__elemento.idade) + "; " + self.__elemento.cidade +
            "; " + self.__elemento.estado])
        return self

    def save(self) -> IBuilder:
        """Método de salvamento do relatório."""
        with open(self.ARQUIVO, 'w', newline='') as file:
            writer = csv.writer(file)
            for linha in self.__relatorio:
                writer.writerow(linha)
        return self

    def get_relatorio(self) -> str:
        """Método de retorno do relatório."""
        with open(self.ARQUIVO, 'r') as file:
            leitor = csv.reader(file)
            next(leitor)
            for linha in leitor:
                self.__relatorio.append(linha)
        return self.__relatorio