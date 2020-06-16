def leiaInt(num):
    while True:
        if num.isnumeric():
            return num
        else:
            print('\033[0;31mVocê digitou um número inteiro inválido\033[m')
            num = input('Digite um número: ')


n = leiaInt(input('Digite um número: '))
print(f'Você acabou de digitar o número {n}')