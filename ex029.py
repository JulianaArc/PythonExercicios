velocidade=float(input('Qual é a velocidade atual do carro?:'))
if velocidade>=80:
    print('MULTADO! Você excedeu o limite permitido que é de 80 km/h')
    valor_da_multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(valor_da_multa))
    print('Tenha um bom dia! Dirija com segurança')
else:
    print('Tenha um bom dia! Dirija com segurança')








