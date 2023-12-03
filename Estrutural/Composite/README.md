# Padrão de Projeto Estrutural: Composite
## Índice
- [Sobre](#sobre)
- [Proposito](#proposito)
- [Quando usar](#quando-usar)
- [Pros](#pros)
- [Contras](#contras)

## Sobre:
    - Faz sentido quando você tem que implementar uma estrutura de objetos em forma de árvore.
    - Pode ser a solução para estruturas complexas que podem ser tratadas como uma coleção de objetos semelhantes.

## Proposito
    - Compor objetos em estruturas de árvore para representar hierarquias de partes inteiras e trabalhar com elas como se fossem objetos individuais.

### Quando usar
    - Tem uma estrutura de dados hierárquica que contém objetos e coleções de objetos. E você precisa executar operações em toda a estrutura de dados.
    - Quer que o código cliente trate objetos individuais e composições de objetos uniformemente.

### Pros
    - Você pode trabalhar com estruturas de árvore complexas de maneira simples e intuitiva.
    - Principio de aberto/fechado.

### Contras
    - Pode ser difícil fornecer uma implementação adequada de um componente base da árvore.