from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
for c in range(1, 5):
    jogo[f'Jogador{c}'] = randint(1, 6)
ranking = list()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    sleep(1)
