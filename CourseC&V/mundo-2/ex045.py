import random, time

itens = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0,2)
eu = int(input('Escolha um\n0 - Pedra\n1 - Papel\n2 - Tesoura\nOpção: '))
print('Sorting..\n')
time.sleep(1)

print('Jogador {} X PC {}'.format(itens[eu], itens[pc]))

if pc == 0:
    if eu == 0:
        print('Empate!')
    elif eu == 1:
        print('Jogador venceu!')
    elif eu == 2:
        print('PC venceu!')
    else:
        print('Jogada inválida!!')
elif pc == 1:
    if eu == 0:
        print('PC venceu!')
    elif eu == 1:
        print('Empate!')
    elif eu == 2:
        print('Jogador venceu!')
    else:
        print('Jogada inválida!!')
elif pc == 2:
    if eu == 0:
        print('Jogador venceu!')
    elif eu == 1:
        print('PC venceu!')
    elif eu == 2:
        print('Empate!')
    else:
        print('Jogada inválida!!')
else:
    print('Jogada inválida!')