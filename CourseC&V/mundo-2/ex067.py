valor = 0
cont = 1
while valor >= 0:
    valor = int(input('\nDigite um valor para a tabuada: '))
    if valor < 0:
        break
    for cont in range(1,11):
        print(f'{valor} x {cont} = {valor * cont}')
        cont += 1
print('\nFim do Programa de Tabuada! Always back!!')
