números = []  # Lista para armazenar os números digitados
quantidade = 0
soma = 0

continuar = 'S'
while continuar != 'N':
    if continuar == 'S':
        número = int(input('Digite um número: '))
        quantidade += 1
        #calcular a média
        soma += número  #soma = soma + número
        média = soma / quantidade
        números.append(número)  # Adiciona o número à lista
        continuar = input('Deseja continuar? [S/N]').upper()
    else:
        print('\033[1;31mINVÁLIDO, escolha entre S OU N\033[m')
        continuar = input('Quer continuar? [S/N] ').upper()

print(f'Você digitou {quantidade} números e a média foi {média}')
print(f'O maior valor foi {max(números)} e o menor foi {min(números)}')
