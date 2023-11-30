# Padrão de Projeto Criacional: Prototype
## Índice
- [Sobre](#sobre)
- [Proposito](#proposito)
- [Quando usar](#quando-usar)
- [Pros](#pros)
- [Contras](#contras)

## Sobre:
    - O tipo de objeto a ser criado é determinado em tempo de execução.
    - Usado para evitar a recriação de objetos, quando o custo de criação é alto.
    - Criado com um método clone().
    - Oculta as classes que criam objetos do cliente.

## Proposito
    - Permite copiar objetos existentes sem tornar o código dependente de suas classes.

### Quando usar
    - Deseja ocultar as classes que criam objetos do cliente.
    - Quiser desacoplar o código de criação de objetos do código que usa esses objetos.
    - Quiser evitar a duplicação de código de criação de objetos em seu programa.
    - Tiver muitos campos no objeto e quiser copiá-lo facilmente.

### Pros
    - Permite que o objeto seja clonado e manter o código desacoplado.
    - Pode evitar o código de inicialização, usando o metódio clone().
    - Consegue produzir objetos complexos mais eficientemente.
    - Quiser usar objeto com configurações pré-definidas, em vez de instanciá-los, configurá-los e depois usá-los.

### Contras
    - Objetos com referências circulares podem não ser clonados corretamente.