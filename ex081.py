numeros = list()
while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    r = input('Quer continuar? [S/N] ').upper()
    if r in 'N':
        break
print('-='*30)
print(f'Você digitou {len(numeros)} elementos')
numeros.sort(reverse=True)  # Ordena a lista em ordem decrescente
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')



# OU DE MANEIRA MAIS CONCISA
numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    if input('Quer continuar? [S/N] ').strip().upper() == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(numeros)} elementos')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
print('O valor 5 faz parte da lista!' if 5 in numeros else 'O valor 5 não foi encontrado na lista')
