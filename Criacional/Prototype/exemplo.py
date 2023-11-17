from concrete_product import *

produto_a = Produto().set_preco(12.00).set_descricao("Maçã").set_marca("Hortifruti")
print(id(produto_a))
print(produto_a.get_descricao() + ', ' + produto_a.get_marca() + ', ' + str(produto_a.get_preco()))
produto_b = produto_a.clone()
print(id(produto_b))
produto_b.set_descricao("Banana")
print(produto_a.get_descricao() + ', ' + produto_a.get_marca() + ', ' + str(produto_a.get_preco()))
print(produto_b.get_descricao() + ', ' + produto_b.get_marca() + ', ' + str(produto_b.get_preco()))