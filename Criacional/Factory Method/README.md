# Padrão de Projeto Criacional: Factory Method
## Índice
- [Sobre](#sobre)
- [Proposito](#proposito)
- [Quando usar](#quando-usar)
- [Pros](#pros)
- [Contras](#contras)

## Sobre:
    - Oculta a lógica de instanciação de objetos do código cliente, ficando a cargo da classe fabrica.
    - Usa herança para decidir qual objeto criar, podendo ser criado por uma subclasse ou fabrica.
    - Flexivel para criar objetos, permitindo novas implementações de fabricas sem alterar o código cliente.
    - Pode usar parâmetros para decidir qual objeto criar.

## Proposito
    - Separar a construção de um objeto complexo da sua representação, de modo que o mesmo processo de construção possa criar diferentes representações.

### Quando usar
    - Não souber de antemão os tipos e dependências exatas dos objetos com os quais o código vai trabalhar.
    - Quiser permitir que a suas fabricas sejam estendidas para criar novos tipos de objetos.
    - Quiser desacoplar o código de criação de objetos do código que usa esses objetos.
    - Quiser evitar a duplicação de código de criação de objetos em seu programa.

### Pros
    - Desacopla o seu código.
    - Aplicação do princípio de aberto e fechado.
    - Aplicação do princípio de responsabilidade única.

### Contras
    - Pode ter acumulo de classes, se for usado sem necessidade. Já que deve haver uma classe concreta
    para cada tipo de objeto concreto.