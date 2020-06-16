inicio = int(input('Digite o valor para ser calculado na tabuada: '))

for c in range(1, 11):
    print('{} x {} = {}'.format(inicio, c, inicio * c))
print('FIM TABUADA!')