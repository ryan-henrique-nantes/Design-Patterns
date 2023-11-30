# Padrão de Projeto Criacional: Abstract Factory
## Índice
- [Sobre](#sobre)
- [Proposito](#proposito)
- [Quando usar](#quando-usar)
- [Pros](#pros)
- [Contras](#contras)

## Sobre:
    - Um dos padrôes de projeto criacional.
    - Todo projeto fica mais focado em interfaces e menos em implementação.
    - É uma fábrica, assim como o Factory Method, porém, com a diferença de que a Abstract Factory cria famílias de objetos relacionados.

## Proposito
    - Fornecer uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.
    

### Quando usar
    - Quando um projeto deve ser independente de como seus produtos são criados, compostos e representados.
    - Um projeto deve ser configurado com uma familia de produtos.
    - Deseja fornecer uma biblioteca de classes e quer revelar somente suas interfaces, não implementações.

### Pros
    - Os interfaces são compatíveis entre si.
    - Aplicação clara do princípio de aberto e fechado.
    - Aplicação clara do princípio de responsabilidade única.

### Contras
    - Quanto mais classes, maior a complexidade.