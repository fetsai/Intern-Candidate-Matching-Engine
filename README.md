# Intern-Candidate-Matching-Engine

## Descrição do Projeto
<p align="center">Uma Matching Engine desenvolvida para o processo seletivo para estágio no time de strats do Morgan Stanley. O programa tem como objetivo cruzar ordens em uma exchange de forma rápida e justa.</p>

### Pré-requisitos
A versão do Python utilizada foi a `3.7.6`

### Funcionamento
Ao rodar o programa, já é possível inicial a inserção das ordens no formato:

`<Tipo> <Side> <Price> <Qty>`

Onde:
- Tipo: limit ou market
- Side: buy ou sell
- Price: quando order for limit
- Qty: número de shares

O matching engine procurará a melhor order para realizar o trade, respeitando a chegada destas.

Para parar o programa, enviar `stop`.
