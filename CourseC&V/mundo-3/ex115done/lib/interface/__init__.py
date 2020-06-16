def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[1;33mPrograma interrompido pelo usuário.\033[m')
            return 0
            break
        else:
            return n


def linha(tamanho=55):
    return '-' * tamanho


def cabecalho(txt):
    txt.upper()
    print(linha())
    print(txt.center(55))
    print(linha())


def menu(lista):
    try:
        cabecalho('MENU PRINCIPAL')
        c = 1
        for i in lista:
            print(f'\033[1;33m{c}\033[m - \033[34m{i}\033[m')
            c += 1
        print(linha())
        escolha = leiaInt(f'\033[1;33mSua opção: \033[m')
        return escolha
    except KeyboardInterrupt:
        print(f'\n\033[1;33mPrograma interrompido pelo usuário.\033[m')
