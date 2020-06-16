def titulo():
    titulo = 'SISTEMA DE AJUDA PYTHON'
    tamanho_titulo = len(titulo) + 10
    print(f'\033[30;42m{"~" * tamanho_titulo}\033[m')
    print(f'\033[30;42m{titulo.center(tamanho_titulo)}\033[m')
    print(f'\033[30;42m{"~" * tamanho_titulo}\033[m')


def acesso(acess):
    from time import sleep
    titulo_acesso = f'Acessando o manual do comando {acess}'
    tamanho_acesso = len(titulo_acesso) + 10
    print(f'\033[30;44m{"~" * tamanho_acesso}\033[m')
    print(f'\033[30;44m{titulo_acesso.center(tamanho_acesso)}\033[m')
    print(f'\033[30;44m{"~" * tamanho_acesso}\033[m')
    sleep(2)


def ajuda(func):
    acesso(func)
    print()
    print(f'\033[7;30m')
    help(func)
    print(f'\033[m')


# Programa Principal
comando = ''
while True:
    titulo()
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
