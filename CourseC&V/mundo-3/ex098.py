from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-' * 50)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2.5)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print(f'FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 50)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início:   '))
fi = int(input('Fim:      '))
pas = int(input('Passo:    '))
contador(ini, fi, pas)
