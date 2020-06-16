escolha = ''
cont_maior = 0
cont_homens = 0
cont_mulher_menos20 = 0

while escolha in 'Ss':

    sexo = input('Sexo [M/F]: ').upper().strip()[0]
    while sexo not in 'MmFf':
        print('Favor inserir um valor correto [M/F]!')
        sexo = input('\nSexo [M/F]: ').upper().strip()[0]

    idade = int(input('Idade: '))
    if idade >= 18:
        cont_maior += 1
    if sexo in 'Mm':
        cont_homens += 1
    if sexo in 'Ff' and idade < 20:
        cont_mulher_menos20 += 1

    escolha = input('\nDeseja continuar? [S/N] ').upper().strip()[0]
    if escolha not in 'Nn' and escolha not in 'Ss':
        while escolha not in 'Nn' and escolha not in 'Ss':
            print('Favor inserir um valor correto [S/N]!')
            escolha = input('\nDeseja continuar? [S/N] ')

    if escolha in 'Nn':
        break
print(f'\nFIMMMMM\n\nPessoas +18: {cont_maior}\nHomens: {cont_homens}\nMulheres -20: {cont_mulher_menos20}')
