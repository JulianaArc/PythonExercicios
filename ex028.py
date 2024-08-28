import random
from time import sleep  #faz o computador esperar
print('vou pensar em um número entre 0 e 5. tente adivinhar...')
sleep(1)
n=int(input('em que número eu pensei?:'))
print('processando...')
sleep(2)
número_sorteado=random.randint(0, 5)
print('parábens você ganhou' if n==número_sorteado else 'GANHEI! eu pensei no número {}, não no número {}'.format(número_sorteado,n))







#ou

import random

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
n = int(input('Em que número eu pensei?: '))
número_sorteado = random.randint(0, 5)
if n == número_sorteado:
    print('Parabéns! Você ganhou.')
else:
    print('Que pena! Eu pensei no número {}, não no número {}.'.format(número_sorteado, n))








