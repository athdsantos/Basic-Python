from random import randint
t = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Números gerados: {t}')
print(f'O maior valor sorteado foi {max(t)} e o menor valor foi {min(t)}')

'''newT = sorted(t)
print(f'Em ordem: {newT}')
print(f'O menor valor sorteado foi {newT[0]} e o maior número sorteado foi {newT[4]}')'''