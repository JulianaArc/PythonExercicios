soma_idades = 0  # Inicializa a variável para armazenar a soma das idades
idade_homem_mais_velho = 0 # Inicializa a idade do homem mais velho encontrado até agora
nome_homem_mais_velho = ""  # Inicializa o nome do homem mais velho encontrado até agora
tot_mulheres_com_menos_de_20 = 0  # Inicializa a variável de mulheres com menos de 20 anos

for c in range(1, 5):
    nome = input(f'-----{c}ª pessoa-----\nNome: ').strip().upper()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()


    soma_idades += idade  # Adiciona a idade da pessoa à soma das idades
    média_idades = soma_idades / c  # Calcula a média das idades


    # Verifica se a pessoa é do sexo masculino ('M') e se sua idade é maior que a idade do homem mais velho encontrado até agora
    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade  # Atualiza a idade do homem mais velho encontrado até agora com a idade dessa pessoa
        nome_homem_mais_velho = nome # Atualiza o nome do homem mais velho encontrado até agora com o nome dessa pessoa

    # Verifica se a pessoa é do sexo feminino ('F') e se tem menos de 20 anos e adiciona +1 a variável tot_mulheres_com_menos_de_20
    elif sexo == 'F' and idade < 20:
        tot_mulheres_com_menos_de_20 += 1 #ou tot_mulheres=tot_mulheres+1


print(f'A média de idade do grupo é de {média_idades} anos')
print(f'O homem mais velho tem {idade_homem_mais_velho} anos e se chama {nome_homem_mais_velho}')
print(f'Ao todo são {tot_mulheres_com_menos_de_20} mulheres com menos de 20 anos')


# NOTA SOBRE MANIPULAÇÃO DE STRINGS
# Ao converter o sexo para maiúsculas utilizando strip().upper(), estamos garantindo que não importa se o usuário inserir "m" ou "M" (ou "f" ou "F"),
# o programa sempre irá interpretar como "M" para masculino e "F" para feminino.
# Isso torna o programa mais robusto e evita erros de interpretação devido a diferentes formas de entrada do usuário.


















