print('='*30)
print('BANCO CEV'.center(30))
print('='*30)

#Solicita o valor de saque ao usuário
saque = int(input('Que valor você quer sacar? R$ '))

# Inicializa a contagem de notas de cada denominação
n50 = n20 = n10 = n1 = 0

# Loop para calcular a quantidade de notas de cada valor
while saque > 0:
    # Verifica se ainda é possível retirar notas de 50
    if saque >= 50:
        n50 += 1
        saque -= 50
    # Verifica se ainda é possível retirar notas de 20
    elif saque >= 20:
        n20 += 1
        saque -= 20
    # Verifica se ainda é possível retirar notas de 10
    elif saque >= 10:
        n10 += 1
        saque -= 10
    # Verifica se ainda é possível retirar notas de 1
    else:
        n1 += 1
        saque -= 1

# Imprime a quantidade de notas de cada denominação usada
print(f'Total de {n50} de R$50')
print(f'Total de {n20} de R$20')
print(f'Total de {n10} de R$10')
print(f'Total de {n1} de R$1')


# OU RESOLUÇÃO DO PROFESSOR

print('='*30)
print('BANCO CEV'.center(30))
print('='*30)
saque = int(input('Que valor você quer sacar? R$ '))
total = saque
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break





