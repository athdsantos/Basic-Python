numeros = []
while True:
    n = int(input('Digite o número: '))
    numeros.append(n)
    escolha = str(input('Parar? [S/N] ')).upper().strip()[0]
    if escolha == 'S':
        break
numeros.sort(reverse=True)
print(f'Foram digitados {len(numeros)} números!')
print(f'Lista de números em ordem decrescente {numeros}')
if 5 in numeros:
    print(f'O número 5 faz parte da lista!')
else:
    print(f'O número 5 não existe na lista!')
