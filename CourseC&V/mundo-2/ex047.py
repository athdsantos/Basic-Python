from time import sleep
print('Calculando números pares entre 1 - 50\n')

numPar = 0

for c in range(0, 51, 2):
    if c % 2 == 0:
        print('{}, '.format(numPar), end=' ')
        numPar += 2
print('FIM!')
