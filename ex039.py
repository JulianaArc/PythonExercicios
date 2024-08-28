import datetime
nascimento = int(input('ano de nascimento:'))
ano_atual = datetime.datetime.now().year
idade = ano_atual - nascimento
print(f'quem nasceu em {nascimento} tem {idade} anos em {ano_atual}')
if idade == 18:
    print('você tem que se alistar \033[1;31mIMEDIATAMENTE!\033[m')

elif idade < 18: #se a idade for menor que 18
    X = 18 - idade #calcula quanto falta para o alistamento
    print(f'ainda faltam {X} anos para o alistamento')

elif idade > 18: #se a idade for maior que 18
    Q = idade - 18 #calcula há quanto tempo já deveria ter se alistado
    print(f'você já deveria ter se alistado há {Q} anos')
    print(f'seu alistamento foi em {ano_atual - Q}') #calcula em que ano foi alistamento











