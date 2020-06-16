numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print(f'Número {n} adicionado com sucesso à lista!')
    elif n in numeros:
        while n in numeros:
            print(numeros)
            n = int(input('Valor existente, favor digitar inexistente: '))
        numeros.append(n)
    print(numeros)
    escolha = str(input('Deseja continuar [S/N]? ').upper().strip()[0])
    while escolha not in 'SN':
        escolha = str(input('Digite um valor válido, deseja continuar [S/N]? ').upper().strip()[0])
    if escolha in 'Nn':
        break
print(f'A lista final de números é {sorted(numeros)}')
