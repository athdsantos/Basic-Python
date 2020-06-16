from random import randint
from time import sleep

numeros = list()

def sorteio():
    print('Sorteando os 5 valores da lista: ', end='')
    while len(numeros) != 5:
        numeros.append(randint(1, 10))
    print(f'{numeros}')

def somaPar(listaNumeros):
    soma = 0
    for k, v in enumerate(listaNumeros):
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {numeros}, temos o total de {soma}')


sorteio()
somaPar(numeros)
