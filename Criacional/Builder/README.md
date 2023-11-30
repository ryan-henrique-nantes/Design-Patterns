# Padrão de Projeto Criacional: Builder
## Índice
- [Sobre](#sobre)
- [Proposito](#proposito)
- [Quando usar](#quando-usar)
- [Pros](#pros)
- [Contras](#contras)

## Sobre:
    - O projeto sugere a separação da construção de um objeto de aonde ele é usado.
    - Trata de construir objetos complexos passo a passo.
    - Permite o uso de chaining e programação fluente.
    - É um padrão complexo.

## Proposito
    - Separar a construção de um objeto complexo da sua representação, de modo que o mesmo processo de construção possa criar diferentes representações.
    
### Quando usar
    - Tiver um objeto muito complexo para ser criado em uma única função, ou seja, quando o objeto possui muitos atributos.
    - Quando a construção de um objeto precisa ser independente da representação dele.
    - Quando quiser que o código seja capaz de criar diferentes representações de algum objeto complexo.

### Pros
    - Você consegue gerenciar o processo de construção passo a passo e criar objetos complexos.
    - Reutilizar código de construção entre diferentes objetos.
    - Aplicação clara do princípio de responsabilidade única.

### Contras
    - O código fica mais complexo em geral, pela necessidade de criar várias classes.