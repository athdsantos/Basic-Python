numeros = []
numImpar = []
numPar = []
while True:
    n = int(input('Digite um valor [-1 para sair]: '))
    if n == -1:
        break
    numeros.append(n)
    if n % 2 == 0:
        numPar.append(n)
        # print(f'O número {n} é par, adicionado a lista par com sucesso!')
    else:
        numImpar.append(n)
        # print(f'O número {n} é ímpar, adicionado a lista ímpar com sucesso!')
print(f'Inteira {numeros}\nÍmpares {numImpar}\nPares {numPar}')
