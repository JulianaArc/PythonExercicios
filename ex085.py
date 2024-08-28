núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:  # se for par
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-='*30)
núm[0].sort()  # colocar em ordem crescente
núm[1].sort()
print(f'os valores pares digitados foram: {núm[0]}')
print(f'os valores ímpares digitados foram: {núm[1]}')

