'''from math import factorial

num = int(input('Digite um número para Fatorial: '))
print(factorial(num))'''

fatorial = int(input('Digite um número: '))
contador = fatorial
fator = 1
while contador != 0:
    print(contador)
    fator *= contador
    contador -= 1
print(fator)
