count = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze',
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        print(f'Você digitou o número {count[núm]}')
        continuar = input('Quer continuar? [S/N] ').strip().upper()
        if continuar == 'N':
            break
    else:
        print('Tente novamente.', end='')
