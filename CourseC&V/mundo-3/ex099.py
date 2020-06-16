from time import sleep


def numMaior(* num):
    maior = cont = 0
    print('-' * 50)
    print(f'Analisando os valores passados..')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo!')
    print(f'O maior valor informado foi {maior}')

numMaior(2, 9, 4, 5, 7, 1)
numMaior(4, 7, 0)
numMaior(1, 2)
numMaior(6)
numMaior()