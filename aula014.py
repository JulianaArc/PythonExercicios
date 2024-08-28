# aula 14: ESTRUTURA DE REPETIÇÃO WHILE

# diferença entre FOR E WHILE

# 1. For Loop:
# Um loop for é usado quando você sabe antecipadamente quantas vezes deseja executar um bloco de código.

# 2. While Loop:
# Um loop while é usado quando você não sabe quantas vezes precisa executar um bloco de código
# e deseja continuar a executá-lo enquanto uma condição especificada for verdadeira.
# É útil quando o número de iterações não é conhecido antecipadamente e depende de uma condição específica.

n = 1   # n começa em 1
while n != 0:   # enquanto n for diferente de 0
    n = int(input('digite um valor: '))
print('fim')


r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('quer continuar? [S/N] ')).upper()
print('fim')
