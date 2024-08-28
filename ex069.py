print('-' * 30)
print('CADASTRE UMA PESSOA'.center(30))
print('-' * 30)
total_de_pessoas_maior_18 = 0
total_homens_cadastrados = 0
total_de_mulheres_cadastradas = 0
total_mulheres_menos_20 = 0
while True:
    Idade = int(input('Idade: '))
    Sexo = ' '
    while Sexo not in 'MF':       ## Loop para solicitar o sexo até que seja fornecida uma entrada válida ('M' ou 'F')
        Sexo = input('Sexo: [M/F] ').strip().upper()[0]
        if Sexo not in 'MF':      ## Verifica se a entrada do usuário não é 'M' nem 'F'
            print('Por favor, digite apenas M ou F.')
    print('-' * 30)
    if Idade > 18:
        total_de_pessoas_maior_18 += 1
    if Sexo == 'M':
        total_homens_cadastrados += 1
    elif Sexo == 'F':
        total_de_mulheres_cadastradas += 1
        if Idade < 20:  # Ajuste da condição para verificar mulheres com menos de 20 anos
            total_mulheres_menos_20 += 1
    continuar = input('Quer continuar? [S/N] ').upper()
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total_de_pessoas_maior_18}')
print(f'Ao todo temos {total_homens_cadastrados} homens cadastrados')
print(f'Ao todo temos {total_de_mulheres_cadastradas} mulheres cadastradas')
print(f'E temos {total_mulheres_menos_20} mulheres com menos de 20 anos')

