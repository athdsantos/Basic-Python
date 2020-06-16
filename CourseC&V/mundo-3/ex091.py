from random import randint
from time import sleep
from operator import itemgetter
#OUTRA FORMA DE FAZER -> jogadores = {'jogador1': ,randint(1, 6), 'jogador2': 0 ,randint(1, 6), 'jogador3': ,randint(1, 6), 'jogador4':  ,randint(1, 6),}
jogadores = {'jogador1': 0, 'jogador2': 0, 'jogador3': 0, 'jogador4': 0}
ranking = list()
i = 1
while i <= len(jogadores):
    for j in jogadores:
        jogadores[j] = randint(1, 6)
    print(f'{"VALORES SORTEADOS":^29}')
    print('-=' * 15)
    sleep(2)
    for k, j in jogadores.items():
        print(f'{"":>6}O {k} tirou {j}')
        sleep(1)
    ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
    print()
    print('-=' * 15)
    print(f'{"RANKING DOS JOGADORES":^29}')
    print('-=' * 15)
    for i, v in enumerate(ranking):
        print(f'{"":^2}{i + 1}º lugar: {v[0]} com {v[1]}')
        sleep(1)
    break
