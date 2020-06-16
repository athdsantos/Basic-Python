valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
escolha = 0
while escolha != 5:
    print('''\n         MENU
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair
    ''')
    escolha = int(input('Digite sua opção: '))

    if escolha == 1:
        print('\nSOMA\n{} + {} = {}\n'.format(valor1, valor2, valor1 + valor2))
    elif escolha == 2:
        print('\nMULTIPLICAÇÃO\n{} x {} = {}'.format(valor1, valor2, valor1 * valor2))
    elif escolha == 3:
        print('\nMAIOR')
        if valor1 > valor2:
            print('O valor {} é maior que o valor {}.'.format(valor1, valor2))
        elif valor2 > valor1:
            print('O valor {} é maior que o valor {}.'.format(valor2, valor1))
        else:
            print('Empate, os valores {} e {} são iguais!'.format(valor1, valor2))
    elif escolha == 4:
        print('\nNOVOS NÚMEROS\n')
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite outro valor: '))
    elif escolha == 5:
        print('Byee!!')
    else:
        print('Valor incorreto, digite um valor válido!')
