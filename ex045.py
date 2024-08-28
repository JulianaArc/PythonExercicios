from time import sleep
import random
print('Suas opções')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jogador = int(input('qual é a sua jogada? '))
sleep(1)
print('PEDRA...')
sleep(1)
print('PAPEL...')
sleep(1)
print('TESOURA!')
sleep(1)
opções = ['PEDRA', 'PAPEL', 'TESOURA']
opção_escolhida_computador = random.choice(opções)
print('-=' * 15)
print(f'computador jogou {opção_escolhida_computador}')
print(f'jogador jogou {opções[jogador]}')
print('-=' * 15)
if opção_escolhida_computador == opções[jogador]:
    print('EMPATE')
elif (opção_escolhida_computador == 'PEDRA' and opções[jogador] == 'TESOURA') or \
        (opção_escolhida_computador == 'PAPEL' and opções[jogador] == 'PEDRA') or \
        (opção_escolhida_computador == 'TESOURA' and opções[jogador] == 'PAPEL'):
    print('COMPUTADOR VENCEU !!!')
else:
    print('JOGADOR VENCEU !!!')


