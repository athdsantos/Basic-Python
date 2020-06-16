numeros = []
for cont in range(5):
    numeros.append(int(input('Digite um número: ')))
print(f'Valores na lista de números: {numeros}')
print(f'O maior valor digitado foi o {max(numeros)} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == max(numeros):
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi o {min(numeros)} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == min(numeros):
        print(f'{i}... ', end='')
print()
