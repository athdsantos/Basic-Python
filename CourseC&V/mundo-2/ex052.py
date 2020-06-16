num = int(input('Digite um número inteiro: '))
print('Verificando os números primos..')
numPrimo = 0
for c in range(1, num + 1):
    if num % c == 0:
        numPrimo += 1
if numPrimo == 2:
    print('{} é primo'.format(num))
else:
    print('{} não é primo!'.format(num))
print('FIM!')
