pessoas = []
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    pessoas.append([nome, peso])
    c = input('Quer continuar? [S/N] ').upper()
    if c == 'N':
        break

print('-=' * 30)

print(f'Ao todo você cadastrou {len(pessoas)} pessoas')

# Inicializa as variáveis para encontrar os maiores e menores pesos
maior_peso = max(pessoas, key=lambda p: p[1])[1]
menor_peso = min(pessoas, key=lambda p: p[1])[1]

print(f'O maior peso foi de {maior_peso}Kg. Peso de', end=' ')
for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        print(f'{pessoa[0]}', end=' ')
print()

print(f'O menor peso foi de {menor_peso}Kg. Peso de', end=' ')
for pessoa in pessoas:
    if pessoa[1] == menor_peso:
        print(f'{pessoa[0]}', end=' ')
print()
