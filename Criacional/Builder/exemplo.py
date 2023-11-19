from concrete_director import *
from concrete_product import *

for linha in Director.new().build(Funcionario.new().set_nome("João").set_idade(20).set_estado("MS").set_cidade("Campo Grande")):
    print(linha)