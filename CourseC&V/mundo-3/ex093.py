jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
qtdPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for g in range(qtdPartidas):
    gol = int(input(f'Quantos gols {jogador["nome"]} fez na partida {g + 1}? '))
    gols.append(gol)
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
print('-=' * 30)
print(f'{jogador}')
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {qtdPartidas} partidas.')
for c, v in enumerate(gols):
    print(f'{"":>5} => Na partida {c + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols!')
