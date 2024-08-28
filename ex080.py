import bisect  # Importa a biblioteca bisect que ajuda a inserir elementos em uma lista mantendo-a ordenada

numeros = []  # Inicializa uma lista vazia para armazenar os valores

# Loop para capturar 5 valores do usuário
for c in range(5):
    n = int(input('digite um valor: '))  # Solicita ao usuário que digite um valor e converte para inteiro
    bisect.insort(numeros, n)  # Insere o valor na posição correta na lista para mantê-la ordenada
    print(f'numero {n} adicionado na posição {numeros.index(n)}')  # Imprime o valor adicionado e a posição onde foi inserido

# Após todos os valores terem sido inseridos, imprime a lista completa em ordem
print(f'Os valores digitados em ordem foram: {numeros}')


#NOTAS
# A biblioteca bisect é importada para usar suas funções, que são úteis para inserir elementos de forma que a lista permaneça sempre ordenada.
# A palavra "bisect" significa "bisectar" ou "dividir em duas partes"

#"Insort" vem da combinação de "insert" (inserir) e "sort" (ordenar).

#Explicando o INDEX
# Exemplo simples:
# Suponha que você tenha a seguinte lista de frutas:
# frutas = ['maçã', 'banana', 'cereja', 'banana', 'kiwi']
# Se você quiser saber em que posição a 'banana' aparece pela primeira vez, você usa:
# posicao_banana = frutas.index('banana')
# print(f'A primeira banana está na posição {posicao_banana}')
# Isso imprimirá:
# A primeira banana está na posição 1

# No seu código, você está adicionando números a uma lista de forma que ela fique ordenada.
# Depois de adicionar um número, você usa index para mostrar em qual posição o número foi inserido.
# Isso ajuda a confirmar que o número foi adicionado corretamente e onde ele se encontra na lista.