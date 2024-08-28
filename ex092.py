import datetime

# Dicionário para armazenar os dados do trabalhador
Ct = {}

# Coleta de dados
Ct['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
Ct['idade'] = datetime.datetime.now().year - nascimento
Ct['carteira de trabalho'] = int(input('Carteira de trabalho (0 não tem): '))

# Se a carteira de trabalho não for 0, coleta mais dados
if Ct['carteira de trabalho'] != 0:
    Ct['ano de contratação'] = int(input('Ano de contratação: '))
    Ct['salário'] = float(input('Salário: '))
    Ct['aposentadoria'] = (Ct['ano de contratação'] + 35) - nascimento

# Exibição dos dados
print('-=' * 30)
for k, v in Ct.items():
    print(f' - {k} tem o valor {v}')





