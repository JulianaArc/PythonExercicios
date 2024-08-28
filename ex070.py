print('-'*50)
print('LOJA SUPER BARATÃO'.center(50))
print('-'*50)

total_das_compras = 0
custa_mais_de_1000 = 0
preço_mais_barato = float('inf')  # Inicialize com um valor infinitamente alto positivo
produto_mais_barato = ''  # Inicialize com uma string vazia

while True:
    nome_do_produto = input('Nome do Produto: ')
    preço = float(input('Preço: '))
    total_das_compras += preço

    # Verifica se o preço é maior que R$1000.00
    if preço > 1000:
        custa_mais_de_1000 += 1

    # Verifica se o preço é o mais barato até agora e também o nome do produto
    if preço < preço_mais_barato: #se preço for menor que preço_mais_barato
        preço_mais_barato = preço
        produto_mais_barato = nome_do_produto

    continuar = input('Quer continuar? [S/N] ').upper()
    if continuar == 'N':
        break
print('-----------FIM DO PROGRAMA-----------')
print(f'O total da compra foi R${total_das_compras:.2f}')
print(f'Temos {custa_mais_de_1000} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_mais_barato} que custa R${preço_mais_barato:.2f}')


#EXPLICAÇÕES IMPORTANTES
# inicializamos preco_mais_barato com um valor muito alto (float('inf'))
# Em Python, float('inf') representa o infinito positivo. Isso significa que é um número maior do que qualquer outro número real.
# Quando usamos float('inf') para inicializar preco_mais_barato, estamos garantindo que qualquer preço que encontrarmos no loop
# será menor que preco_mais_barato inicialmente, pois nenhum preço real pode ser igual ou maior que infinito.

# Então, durante o loop, quando encontramos um preço que é menor do que preco_mais_barato (e vamos encontrar, já que ele está como valor infinito),
# atualizamos preco_mais_barato com esse novo preço. No final do loop, preco_mais_barato conterá o menor preço entre todos os preços que encontramos até agora.


# NÃO ENTENDEU? VAMOS PARA UM EXEMPLO PRÁTICO:

# Vamos considerar o valor infinito positivo (float('inf')) como sendo 1000 mil
# e digamos que os preços que eu digite sejam 800, 700, 600:
# se durante o loop ele vai encontrar um preço que é menor que ele, poderia ser qualquer um desses,
# inclusive fazendo mais sentido ser o 800, então de que maneira ele sabe que é o 600?

# A explicação se trata de ordem de digitação:
# nesse exemplo, se os preços digitados forem 800, 700 e 600,
# preco_mais_barato será atualizado para 800 quando encontrarmos esse preço, mas quando encontrarmos 700, ele será atualizado para 700,
# e finalmente, quando encontrarmos 600, preco_mais_barato será atualizado para 600. Portanto, no final do loop, preco_mais_barato conterá o menor preço encontrado.

# ou seja, vai atualizando conforme digitado o prox valor, e salva o menor deles.

# Então, pra fixar:
# # Durante o loop, verificamos se o preço atual digitado é menor que preco_mais_barato.
# Se for, atualizamos preco_mais_barato e produto_mais_barato com os valores atuais.
