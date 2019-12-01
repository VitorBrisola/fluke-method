# Fluke Method
Fluke Method é uma aplicação construida para simular a designação de chamadas entre 3 níveis de funcionários: Atendente, Especialista e Revisor.

## Solução
Considerando o problema acima a seguinte lógica foi implementada como solução:

1. 3 pilhas diferentes, uma pra cada cargo, são usadas para determinar a disponibilidade dos funcionários.
2. 1 pilha é utilizada para armazenar funcionários não disponíveis
3. As pilhas de funcionários disponíveis são checadas em ordem de cargo (atendente,especialista e, por fim, revisor), quando uma pilha está vazia a próxima é checada.
4. Ao receber uma ligaçao o funcionário passa de disponível para indisponível
5. Quando uma ligação chega ao revisor, a disponibilidade de funcionários é checada novamente, trocando-os de pilhas quando necessário, e a ligação é repassada do revisor para o próximo funcionário disponível.

## Lógica de implementação
Além do algoritmo utilizado acima e os metodos necessários para implementa-lo, foi-se utilizada apenas uma única classe (funcionário). A ideia inicial era a extensão de classes filhas apartir desta classe principal, porém não foi encontrada necessidade de desenvolvê-las para resolver o problema em questão.

