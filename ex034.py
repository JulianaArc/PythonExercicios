salário = float(input('qual é o salário do funcionário? R$:'))
if salário <= 1250:
    aumento = (salário * 15) / 100   #aumento_de_15%
else:
    aumento = (salário * 10) / 100   #aumento_de_10%

novo_salário = salário + aumento
print('quem ganhava {:.2f} passa a ganhar {:.2f} agora.'.format(salário,novo_salário))









