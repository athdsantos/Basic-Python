numeros = [[], []]
valor = 0
for c in range(7):
    valor = int(input(f'Digite o {c + 1}º numero: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print(f'Pares {sorted(numeros[0])}\nÍmpares {sorted(numeros[1])}')
