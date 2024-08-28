opção = 0
while opção != 5:  # Enquanto a opção selecionada não for 5, o loop continuará
    n1 = float(input('primeiro valor: '))
    n2 = float(input('segundo valor: '))
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opção = int(input('Qual é sua opção: '))
    if opção == 1:
        resultado = n1 + n2
        print(f'O resultado de {n1:.0f} + {n2:.0f} é {resultado:.0f}')
    elif opção == 2:
        resultado = n1 * n2
        print(f'O resultado de {n1:.0f} x {n2:.0f} é {resultado:.0f}')
    elif opção == 3:
        resultado = maior = n1 # aqui dizemos que o maior valor é do n1         #OU resultado = max(n1, n2)
        if n2 > n1:  # mas se n2 for maior que n1
            maior = n2  # então maior é n2
        print(f'Entre {n1:.0f} e {n2:.0f} o maior valor é {maior:.0f}')
    elif opção == 4:
        continue  # Volta ao início do loop para permitir que o usuário insira novos números
    elif opção != 5:  # Se a opção escolhida não for 5 nem 1, 2, 3 ou 4 exibe mensagem de erro
        print('Opção inválida. Por favor, escolha uma opção válida.')




# O continue é uma palavra-chave em Python que é usada dentro de loops (while ou for) para pular para a próxima iteração do loop sem executar o restante do código dentro do bloco do loop.
# No código, quando o usuário escolhe a opção 4 (para inserir novos números), a instrução continue é executada.
# Isso faz com que o programa pule imediatamente para o início do loop while, ignorando qualquer código que esteja abaixo do continue.
# Como resultado, o programa volta a solicitar que o usuário insira os novos números, iniciando um novo ciclo de iteração do loop.
# Essencialmente, o continue permite que você retorne ao início do loop antes de terminar a iteração atual, o que é útil quando você deseja ignorar parte do código em certas condições.



