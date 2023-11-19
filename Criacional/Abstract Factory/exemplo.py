from concrete_factory import Factory

factory = Factory.new()

factory.funcionario.set_codigo(1).set_idade(20).set_nome("João")
factory.marca.set_cnpj("123456789").set_nome("Nome").adicionar_funcionario(factory.funcionario)
factory.produto.set_descricao("Produto").set_marca(factory.marca).set_preco(10.0)
print("Marca: " + factory.produto.marca.nome)
print("Funcionario: " + factory.produto.marca.funcionario(1).nome)
factory.marca.funcionario(1).dormir()