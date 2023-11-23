"""Module client que vai usar o adapter"""

from abstracts import IPassaro, IPassaroBrinquedo
from adapter import PatoDeBorrachaAdapter
from target import Pato
from adaptee import PatoDeBorracha

pato = Pato.new("Pato")
print(pato.voar())
print(pato.granir())
pato_de_borracha = PatoDeBorrachaAdapter.new(PatoDeBorracha.new("Pato de borracha"))
print(pato_de_borracha.voar())
print(pato_de_borracha.granir())
