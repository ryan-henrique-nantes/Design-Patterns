"""Module do Client do padrão Composite."""
from leaf import Viagem
from composite import PacoteViagem

pacote =  PacoteViagem()

pacote.adicionar_viagem(Viagem.new())
pacote.adicionar_viagem(Viagem.new())
pacote.adicionar_viagem(Viagem.new())
pacote.adicionar_viagem(Viagem.new())
print(str(pacote.calcular_valor()))