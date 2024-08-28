from time import sleep
while True:
    print('=' * 50)
    print('GERENCIADOR DE PAGAMENTOS DA LOJA, BEM VINDO!'.center(50))  # centralizar um título usando o método center()
    print('=' * 50)
    print('Por favor press Enter para continuar.')
    input() # Aguarda a pressão da tecla Enter
    preço = float(input('Preço total das compras: R$ '))
    print('FORMAS DE PAGAMENTO')
    print('[ 1 ] à vista dinheiro/cheque')
    print('[ 2 ] no débito cartão')
    print('[ 3 ] 2x no cartão')
    print('[ 4 ] 3x ou mais no cartão')
    opção = int(input('qual é a opção? '))
    print('Um momento por favor...')
    (sleep(2))
    if opção == 1:
        preço_com_desconto = preço - (10 * preço)/100  #desconto de 10% subtraído do preço original
        print(f'a compra de R${preço:.0f} vai custar R${preço_com_desconto:.0f} com desconto de 10%.')
    elif opção == 2:
        preço_com_desconto = preço - (5 * preço)/100 #desconto de 5% subtraído do preço original
        print(f'a compra de R${preço:.0f} vai custar R${preço_com_desconto:.0f} com desconto de 5%.')
    elif opção == 3:
        print(f'sua compra vai custar R${preço:.0f}') #sem desconto
        parcela = preço / 2
        print(f'divido em 2x de R${parcela:.0f}')
    elif opção == 4:
        número_de_parcelas = int(input('quantas parcelas? '))
        parcelas = preço / número_de_parcelas
        preço_total_com_juros = preço + (20 * preço)/100 #juros de 20%
        parcelas_com_juros_20 = preço_total_com_juros / número_de_parcelas
        print(f'sua compra será parcelada em {número_de_parcelas}x de R${parcelas_com_juros_20:.0f} COM JUROS.')
        print(f'sua compra de R${preço:.0f} vai custar R${preço_total_com_juros:.0f} no final')
    else:
        print('\033[1;31mOpção invalida, por favor escolha uns dos números fornecidos!\033[m')

    reiniciar = input('Deseja realizar outra transação? press a tecla (S) para sim e (N) para não: ').strip().upper()
    if reiniciar != 'S':
        break














