from time import sleep
valor = float(input('qual o valor da casa?:'))
salário = float(input('qual o salário do comprador?:'))
financiamento = float(input('quantos anos de financiamento?:'))
print('\033[1mEspere um momento, estamos processando os dados...\033[m')
sleep(3)
calculo_de_meses = financiamento * 12
prestação = valor/calculo_de_meses
print('para pagar uma casa de R${:.0f} em {:.0f} anos a prestação será de \033[31mR${:.2f}\033[m'.format(valor,financiamento,prestação))

#a prestação não pode exceder 30% do salário ou então o empréstimo sera negado.
limite_prestação = (salário * 30) / 100
if prestação > limite_prestação:   #se a prestação for maior que a porcentagem de 30%
    print('\033[1;31mEmpréstimo NEGADO!\033[m')
else:
    print('\033[1;33mEmpréstimo pode ser CONCEDIDO!\033[m')

    #ex: considere o valor da casa 80.000 com financiamento em 7 anos, o que daria uma prestação de 952,38
    # se uma pessoa recebe 1600 o empréstimo será negado, pois 30% de seu sálario é 480
    # logo a prestação (952,38) é maior(>) que (480).






