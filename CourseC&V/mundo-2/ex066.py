cont = 0
soma = 0
num = 0
while num != 999:
    num = int(input('Digite um número [999 para sair]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Números digitados: {cont}\nSoma dos {cont} números inseridos: {soma}.')
