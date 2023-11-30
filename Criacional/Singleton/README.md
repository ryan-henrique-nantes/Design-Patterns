# Padrão de Projeto Criacional: Singleton
## Índice
- [Sobre](#sobre)
- [Proposito](#proposito)
- [Quando usar](#quando-usar)
- [Pros](#pros)
- [Contras](#contras)

## Sobre:
    - As vezes considerado um anti-padrão.
    - Deve ser usado com cuidado.
    - Usado para evitar a recriação de objetos, quando o custo de criação é alto.
    - Geralmente usado como conexão com banco de dados, pois a conexão é cara.

## Proposito
    - Garantir que uma classe tenha apenas uma instância e fornecer um ponto global de acesso para a mesma.

### Quando usar
    - Caso necessite o uso de variaveis globais, o que é uma má prática.
    - Precise de um único objeto compartilhado por diferentes partes do programa.
    - Necessite de um objeto imutável, com uma única instância.
    - Precise de acesso a recursos compartilhados, como banco de dados, interfaces de rede, etc.

### Pros
    - Acesso controlado a instância única.
    - O singleton só é inicializado quando necessário.
    - Substitui variáveis globais.

### Contras
    - Mais difícil de testar.
    - Viola o princípio de responsabilidade única.
    - Requer tratamento especial em ambientes multi-thread.