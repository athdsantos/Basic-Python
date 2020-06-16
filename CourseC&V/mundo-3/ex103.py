def ficha(nome_jogador='<desconhecido>', gols_jogador=0):
    print(f'O jogador {nome_jogador} fez {gols_jogador} gol(s) no campeonato.')


nome = input('Nome do jogador: ')
if nome == '':
    nome = '<desconhecido>'
gols = input('Número de gols: ')
if not gols.isnumeric():
    gols = 0
ficha(nome, gols)