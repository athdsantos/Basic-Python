import time

r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))
print('Verificando..')
time.sleep(1)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar triangulo!')
    time.sleep(1)
    print('Verificando qual o tipo do triângulo..')
    time.sleep(1)
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
    else:
        print('Isóceles!')
else:
    print('Os segmentos não podem formar triangulo!')