termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contador = 0
while contador < 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    contador += 1
print('FIMMM')
