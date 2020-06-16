def leiaInt(num=0):
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[1;33mPrograma interrompido pelo usuário.\033[m')
            return 0
            break
        else:
            return num


def leiaFloat(num=0):
    while True:
        try:
            num = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print('\033[0;31mRRO! Você digitou um número real inválido\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[1;33mPrograma interrompido pelo usuário.\033[m')
            return 0
            break
        else:
            return num


print(f'O valor inteiro digitado foi {leiaInt(0)} e o real foi {leiaFloat(0)}.')
