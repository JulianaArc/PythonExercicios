# LISTAS (# as listas, diferentemente das tuplas, são mutáveis)

num = [2, 5, 9, 1]
num[2] = 3  # o número 9 será substituido pelo 3
print(num)

print('-'*30)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)  # adiciona o número 7 a lista
print(num)

print('-'*30)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()   #coloca os números em ordem crescente
print(num)

print('-'*30)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)  #coloca os números em ordem decrescente
print(num)

print('-'*30)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos') #mostra quantos elementos tem na lista

print('-'*30)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0) #serve para inserir valores na posição desejada, nesse caso estamos inserindo o 0 na posição 2
print(num)
print(f'Essa lista tem {len(num)} elementos')

print('-'*30)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop()  # Vai eliminar o último número da lista
print(num)
print(f'Essa lista tem {len(num)} elementos')

print('-'*30)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop()  # Vai eliminar o último número da lista
num.pop(2)  #vai eliminar o segundo número da lista
print(num)
print(f'Essa lista tem {len(num)} elementos')

print('-'*30)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2) #estamos inserindo o 2 na posição 2
num.remove(2)  # o remove vai eliminar o primeiro 2 da lista
print(num)
print(f'Essa lista tem {len(num)} elementos')

print('-'*30)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')


print('-'*30)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')
print('\n')

print('-'*30)


valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')


print('-'*30)


valores = list()
for count in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')


print('-'*30)

a = [2, 3, 4, 7]
b = a
b[2] = 8  # vai substituir o 4 pelo 8 nas duas listas (até porque igualamos b e a)
print(f'Lista A: {a}')
print(f'Lista B: {b}')


print('-'*30)

a = [2, 3, 4, 7]
b = a[:]  #Nesse caso estamos fazendo uma cópia de tudo que está em a para b (ou seja b não tem ligação alguma com a)
b[2] = 8  # só será substituido o 4 pelo 8 na lista b
print(f'Lista A: {a}')
print(f'Lista B: {b}')





































