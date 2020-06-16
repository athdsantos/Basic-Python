def fatorial(num, show=False):
    """
        -> Calcula o fatorial de um numero
    :param num: O número a ser calculado no fatorial
    :param show: Valor opcional; caso True mostrará o cálculo; Caso fique sem valor, mostrar somente o resulado
    :return: O resultado do fatorial do 'num'
    """
    fat = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= c
    return fat

print(fatorial(3, show=True))
#help(fatorial)
