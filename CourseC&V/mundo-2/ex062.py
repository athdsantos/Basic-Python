termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contador = 0
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar a mais? '))
print('FIM')
