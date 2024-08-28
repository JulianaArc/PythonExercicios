valores = list()   # Inicializa uma lista vazia para armazenar os valores
for c in range(0, 5):   # Loop para capturar 5 valores do usuário
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-'*40)
print(f'Você digitou os valores {valores}')

# Encontrar o maior valor na lista
maior_valor = max(valores)

# Encontrar as posições do maior valor
posicoes_maior_valor = []
for i, v in enumerate(valores):   #'for i' representa as posições dos elementos na lista valores
    if v == maior_valor:
        posicoes_maior_valor.append(i)


# Encontrar o menor valor na lista
menor_valor = min(valores)

# Encontrar as posições do maior valor
posicoes_menor_valor = []
for i, v in enumerate(valores):
    if v == menor_valor:
        posicoes_menor_valor.append(i)

print(f'O maior valor digitado foi {maior_valor} nas posições {posicoes_maior_valor}')
print(f'O menor valor digitado foi {menor_valor} nas posições {posicoes_menor_valor}')



# EXPLICANDO A PARTE DE for i, v in enumerate(valores):
# i recebe o índice (a posição do elemento na lista).
# v recebe o valor do elemento nessa posição.

#Para ilustrar, vamos considerar um exemplo:

#Suponha que valores seja [5, 9, 4, 9, 7].
#O maior valor, maior_valor, é 9.
#O loop for com enumerate funciona assim:

#i = 0, v = 5: v não é igual a 9, então não fazemos nada.
#i = 1, v = 9: v é igual a 9, então adicionamos 1 a posicoes_maior_valor.
#i = 2, v = 4: v não é igual a 9, então não fazemos nada.
#i = 3, v = 9: v é igual a 9, então adicionamos 3 a posicoes_maior_valor.
#i = 4, v = 7: v não é igual a 9, então não fazemos nada.
#Ao final do loop, posicoes_maior_valor será [1, 3], indicando que o maior valor 9 aparece nas posições 1 e 3 da lista valores.
