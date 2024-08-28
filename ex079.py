valores = list()
while True:
     n = int(input('Digite um valor: '))
     if n not in valores:
         valores.append(n)
         print('Valor adicionado com sucesso!')
     else:
         print('Valor duplicado! Não vou adicionar')
     r = input('Quer continuar? [S/N] ').upper()
     if r in 'nN':
         break
valores.sort()  #coloca em ordem crescente
print(f'Você digitou os valores {valores}')
