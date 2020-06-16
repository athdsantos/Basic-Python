def metade(p, formatado=False):
    if formatado:
        return f'{moeda(p / 2)}'
    else:
        return p / 2


def dobro(p, formatado=False):
    if formatado:
        return f'{moeda(p * 2)}'
    else:
        return p * 2


def aumentar(p, porcentagem, formatado=False):
    if formatado:
        return moeda(p + (p * porcentagem / 100))
    else:
        return p + (p * porcentagem / 100)


def diminuir(p, porcentagem, formatado=False):
    if formatado:
        return f'{moeda(p- (p * porcentagem / 100))}'
    else:
        return p - (p * porcentagem / 100)


def moeda(p, moeda_br='R$'):
    return f'{moeda_br}{p:>.2f}'.replace(".", ",")


def resumo(p, porcentagem, porcentagem2):
    msg = 'RESUMO DO VALOR'
    tamanho_msg = len(msg) + 30
    print(f'{"-" * tamanho_msg}\n{msg.center(tamanho_msg)}\n{"-" * tamanho_msg}')
    print(f'Preço analisado \t\t\t{moeda(p)}')
    print(f'Dobro do preço \t\t\t\t{dobro(p, formatado=True)}')
    print(f'Metade do preço \t\t\t{metade(p, formatado=True)}')
    print(f'{porcentagem}% de aumento \t\t\t\t{aumentar(p, porcentagem, formatado=True)}')
    print(f'{porcentagem2}% de redução \t\t\t\t{diminuir(p, porcentagem2, formatado=True)}')
    print('-' * tamanho_msg)