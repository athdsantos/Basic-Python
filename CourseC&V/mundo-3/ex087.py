matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = mai = somColuna = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o valor [{l},{c}]: '))
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]


    print()
print(f'\nSoma de todos os valores pares {somapar}')
for l in range(3):
    somColuna += matriz[l][2]
print(f'A soma da terceira coluna é {somColuna}')
for c in range(3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da 2ª linda é {mai}')
