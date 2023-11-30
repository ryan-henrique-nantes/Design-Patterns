# Padrão de Projeto Estrutural: Adapter
## Índice
- [Sobre](#sobre)
- [Proposito](#proposito)
- [Quando usar](#quando-usar)
- [Pros](#pros)
- [Contras](#contras)

## Sobre:
    - Atual como um adaptador entre duas interfaces incompatíveis.
    - Usado para limitar a interface de uma classe dentro das camadas de aplicação, para que não seja necessário alterar a interface de uma classe quando a interface de outra classe mudar.
    - Usado para adaptar uma interface de um projeto legado para uma nova interface, que o cliente espera.

## Proposito
    - Converter a interface de uma classe em outra interface, que o cliente espera, permitindo que classes com interfaces incompatíveis trabalhem juntas.

### Quando usar
    - Não queira ficar dependente de código de terceiros ou código legado.
    - Deseja usar uma classe existente, mas sua interface não corresponde a interface que você precisa.
    - Quiser reutilizar várias subclasses existentes que não possuem algumas funcionalidades e ficaria muito trabalhoso adicionar essas funcionalidades em cada subclasse.

### Pros
    - Desacopla o cliente da classe adaptada.
    - Usa o princípio de aberto/fechado.
    - Segue o princípio de responsabilidade única.

### Contras
    - Aumenta a complexidade do código.