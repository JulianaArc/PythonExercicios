import random

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

vezes = 0

while True:
    minha_jogada = int(input('Diga um valor: '))
    par_ou_impar = input('Par ou Ímpar? [P/I] ').upper()

    jogada_computador = random.randint(1, 100)  # Escolhe um número aleatório entre 1 e 100
    soma_das_jogadas = minha_jogada + jogada_computador

    # Verifica se a soma das jogadas é par ou ímpar
    resultado = 'PAR' if soma_das_jogadas % 2 == 0 else 'ÍMPAR'  #Se o resto da divisão de um número por 2 for igual a 0, o número é par. Caso contrário, é ímpar.

    # Verifica quem venceu o jogo
    if (par_ou_impar == 'P' and soma_das_jogadas % 2 == 0) or (par_ou_impar == 'I' and soma_das_jogadas % 2 != 0):
        vencedor = 'Você'
    else:
        vencedor = 'Computador'

    print('-' * 15)

    print(f'Você jogou {minha_jogada} e o computador jogou {jogada_computador}. Total de {soma_das_jogadas} DEU {resultado}')

    print('-' * 15)

    if vencedor == 'Você':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=' * 15)
    else:
        print('Você perdeu!')
        print('=' * 15)
        break  # Sai do loop se o jogador perder

    vezes += 1

print(f'GAME OVER, VOCÊ VENCEU {vezes} VEZES.')
