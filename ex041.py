import datetime
nascimento = int(input('ano de nascimento:'))
ano_atual = datetime.datetime.now().year
idade = ano_atual - nascimento
print(f'O atleta tem {idade} anos')
if idade <= 9:  #se a idade for menor ou igual a 9
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:  #se idade for maior que 9 e menor ou igual a 14
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19: #se idade for maior que 14 e menor ou igual a 19
    print('Classificação: JUNIOR')
elif idade > 19 and idade <= 25: #se idade for maior que 19 e menor ou igual a 25
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')


# OU (código mais simplificado)

import datetime
nascimento = int(input('Ano de nascimento: '))
ano_atual = datetime.datetime.now().year
idade = ano_atual - nascimento
print(f'O atleta tem {idade} anos')

if idade <= 9:  # se a idade for menor ou igual a 9
    print('Classificação: MIRIM')
elif idade <= 14:  # se a idade for menor ou igual a 14 (não precisa verificar idade > 9, pois se não for, já será verificada nessa condição)
    print('Classificação: INFANTIL')
elif idade <= 19:  # se a idade for menor ou igual a 19 (não precisa verificar idade > 14, pois se não for, já será verificada nessa condição)
    print('Classificação: JUNIOR')
elif idade <= 25:  # se a idade for menor ou igual a 25 (não precisa verificar idade > 19, pois se não for, já será verificada nessa condição)
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')


