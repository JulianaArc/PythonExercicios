pesos = []  # Inicializa uma lista vazia para armazenar os pesos

for c in range(1, 6):
    peso = float(input(f'peso da {c}ª pessoa: '))
    pesos.append(peso) # Adiciona o peso à lista

print(f'O maior peso lido foi de {max(pesos)}')
print(f'O menor peso lido foi de {min(pesos)}')

