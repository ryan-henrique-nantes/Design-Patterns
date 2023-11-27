"""Module do Client do padrão Decorator."""
from concrete_component import Mensagem
from concrete_decorator import DataHoraMensagem

print(DataHoraMensagem.new(Mensagem.new('Olá, mundo!')).enviar())