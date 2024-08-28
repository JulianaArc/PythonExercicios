while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num <= 0:  # se for menor ou igual a zero, ou seja, negativo
        print('PROGRAMA TABUADA ENCERRADO!')
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
