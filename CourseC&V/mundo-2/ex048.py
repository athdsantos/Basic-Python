from time import sleep

print('Soma de números ímpares entre 1 - 500\n')
somaImpar = 0
cont = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        cont += 1
        somaImpar += c
print('Processando..')
sleep(2)
print('{} valores\nTotal: {}'.format(cont, somaImpar))
