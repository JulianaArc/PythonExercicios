import datetime

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = datetime.datetime.now().year  # Obtém o ano atual se for inserido 0

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):     #ano % 4 == 0 verifica se o ano é divisível por 4. Se o resto da divisão for zero, isso significa que o ano é divisível por 4.
    print(f'{ano} é um ano bissexto.')                        #ano % 100 != 0 verifica se o ano é divisível por 100. Se o resto da divisão for diferente de zero, isso significa que o ano não é divisível por 100.
else:                                                         #ano % 400 == 0 verifica se o ano é divisível por 400. Se o resto da divisão for zero, isso significa que o ano é divisível por 400.
    print(f'{ano} não é um ano bissexto.')
    









