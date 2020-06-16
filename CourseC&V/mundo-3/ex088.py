from random import randint
temp = []
jogos = []
totJogos = 1
qtdJogos = int(input('Quantos jogos quer sortear? '))
while totJogos <= qtdJogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
            cont += 1
        if cont >= 6:
            break
    temp.sort()
    jogos.append(temp[:])
    temp.clear()
    totJogos += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
