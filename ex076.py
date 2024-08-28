# Definindo a tupla com itens e seus respectivos preços
listagem = ('Lápis', 1.74,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livros', 34.90)

print('-' * 40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-' * 40)

for lista in range(0, len(listagem)):
    if lista % 2 == 0:    # Índice par: imprime o nome do item
        print(f'{listagem[lista]:.<30}', end='')
    else:       # Índice ímpar: imprime o preço do item
        print(f'R${listagem[lista]:>7.2f}')

print('-' * 40)








