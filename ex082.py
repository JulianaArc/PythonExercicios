numeros = []
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    r = input('Quer continuar? [S/N] ').upper()
    if r == 'N':
        break
print('-='*30)
print(f'A lista completa é {numeros}')

# Inicializa a lista de números pares
numeros_pares = []
# Verifica e adiciona números pares à lista de pares
for n in numeros:
    if n % 2 == 0:  # Verifica se o número é par
        numeros_pares.append(n)
print(f'A lista de pares é {numeros_pares}')

numeros_impares = []
for n in numeros:
    if n % 2 != 0: # varifica se o número é ímpar
        numeros_impares.append(n)
print(f'A lista de ímpares é {numeros_impares}')





# OU DE FORMA MAIS CONCISA:
numeros = []
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    r = input('Quer continuar? [S/N] ').upper()
    if r == 'N':
        break

print('-=' * 30)
print(f'A lista completa é {numeros}')

# Inicializa as listas de números pares e ímpares
numeros_pares = []
numeros_impares = []

# Verifica e adiciona números pares ou ímpares às respectivas listas
for n in numeros:
    if n % 2 == 0:  # Verifica se o número é par
        numeros_pares.append(n)
    else:  # Se não for par, é ímpar
        numeros_impares.append(n)

print(f'A lista de pares é {numeros_pares}')
print(f'A lista de ímpares é {numeros_impares}')