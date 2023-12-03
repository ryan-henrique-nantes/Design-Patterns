# Padrão de Projeto Estrutural: Decorator
## Índice
- [Sobre](#sobre)
- [Proposito](#proposito)
- [Quando usar](#quando-usar)
- [Pros](#pros)
- [Contras](#contras)

## Sobre:
    - Usa composição ao invés de herança para estender o comportamento de um objeto.
    - Parecido com Composite, porém com intenções diferentes.
    - Adiciona novas responsabilidades a um objeto dinamicamente.
    - Finge ser um objeto decorado, poderiam repassar as chamadas de métodos para o objeto decorado original.
    - Pode manipular dados antes do retorno

## Proposito
    - Implementar novas funcionalidades em um objeto sem alterar seu código original, colocando dentro de um objeto decorador que contém o objeto original.

### Quando usar
    - Precisa adicionar funcionalidades a um objeto de forma dinâmica e transparente, sem afetar outros objetos.
    - Quando é complicado ou impossível estender o comportamento de um objeto usando herança.

### Pros
    - Pode estender o comportamento de um objeto sem usar herança.
    - Pode adicionar ou remover responsabilidades de um objeto durante o tempo de execução.
    - Pode combinar vários comportamentos usando vários decoradores.
    - Principio da responsabilidade única.

### Contras
    - É difícil remover um decorador específico da pilha de decoradores.
    - É difícil implementar um decorador de forma que seu comportamento não dependa da ordem de empilhamento dos decoradores.
    - A configuração inicial do decorador pode se tornar complicada.