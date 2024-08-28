#LISTAS (PARTE 2)
teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

print('-'*30)

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()  #outra lista
galera.append(teste) #colocando a lista teste dentro da lista galera
print(galera)  #vai mostrar uma lista dentro da outra

print('-'*30)

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #Nesse caso estamos fazendo uma cópia de tudo que está em teste para galera
teste[0] = 'Maria'  #mudei de 'Gustavo' pra 'Maria
teste[1] = 22    #mudei de 40 pra 22
galera.append(teste[:])
print(galera)

print('-'*30)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]  #4 estruturas compostas dentro de uma estrutura
print(galera)

print('-'*30)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]  #4 estruturas compostas dentro de uma estrutura
print(galera[0])  #vai mostrar os dados do joão

print('-'*30)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]  #4 estruturas compostas dentro de uma estrutura
print(galera[0][0])  #vai mostrar apenas o nome 'João'

print('-'*30)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]  #4 estruturas compostas dentro de uma estrutura
print(galera[2][1])  #vai mostrar apenas a idade de joaquim '13'

print('-'*30)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera: #para cada pessoa em galera
    print(p)

print('-'*30)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera: #para cada pessoa em galera
    print(p[0])  #vai mostrar só os nomes

print('-'*30)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera: #para cada pessoa em galera
    print(p[1])  #vai mostrar só as idades

print('-'*30)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

print('-'*30)

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: '))) #li o nome e joguei na lista dado
    dado.append(int(input('Idade: '))) #li a idade e joguei na lista dado
    galera.append(dado[:])  #joguei uma copia da lista dado dentro da lista galera
    dado.clear() #dado.clear() é necessário para garantir que a lista dado seja esvaziada, evitando acumulação de dados
print(galera)

print('-'*30)

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera: # para cade pessoa em galera
    if p[1] >= 21: # se a idade for maior ou igual a 21
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'temos {totmai} maiores e {totmen} menores de idade')














































