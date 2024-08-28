# ESTRUTURA DE REPETIÇÃO FOR
for c in range (0,6):   # fará 'oi' 6 vezes
    print('oi')
print('fim')


for c in range(6, 0, -1): # fará DECRESCENTE de 6 a 1
    print(c)
print('FIM')


for c in range(0, 7, 2): # irá de 0 a 6 pulando de 2 em 2
    print(c)
print('FIM')


n = int(input('digite um número'))
for c in range(0, n):
    print(c)
print('FIM')


n = int(input('digite um npumero'))
for c in range(0, n + 1):
    print(c)
print('FIM')


i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
for c in range (i, f+1, p):
    print(c)
print('FIM')


for c in range(0, 3):
    n = int(input('digite um valor'))
print('fim')


s = 0
for c in range(0, 4):
    n = int(input('digite um valor'))
    s = s + n  #ou tbm s+=n
print(f'O somatório de todos os valores foi {s}')
