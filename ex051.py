print(30 * '=')
print('10 TERMOS DE UMA PA'.center(30))
print(30 * '=')
n = int(input('Informe o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
for c in range(0,10):
    pa= n + r * c
    print(pa, end=' -> ')




