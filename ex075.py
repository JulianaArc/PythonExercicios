núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')

if 3 in núm:  # Verifica se o valor 3 está presente na tupla
    print(f'O valor 3 apareceu na posição {núm.index(3) + 1}')   # +1 é adicionado porque as posições em Python começam em 0, mas o desejo é que a contagem comece em 1.
else:
    print('O valor 3 não está presente na tupla.')

contagem_pares = 0  # Inicializa a contagem de valores pares
for valor in núm:
    if valor % 2 == 0:  # Verifica se o valor é par
        contagem_pares += 1  # Incrementa a contagem de valores pares

print(f'Os valores pares foram digitados {contagem_pares} vezes')

# OU TAMBÉM:
#contagem_pares = sum(1 for valor in núm if valor % 2 == 0)
#print(f'Os valores pares foram digitados {contagem_pares} vezes')



# O MOTIVO DO 3 PRECISAR DE UMA VERIFICAÇÃO IF:
# O problema ocorre porque, se o valor 3 não estiver presente na tupla núm, a função index(3) causará um erro.
# Isso acontece porque index(3) tentará encontrar o índice do valor 3 na tupla núm, mas não o encontrará,
# resultando em um erro de "ValueError: tuple.index(x): x not in tuple".
# Para evitar esse erro, podemos adicionar uma verificação para garantir que o valor 3 esteja presente antes de chamar a função index().