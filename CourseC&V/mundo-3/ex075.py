tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')),
         int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Os valores são {tupla}')
print(f'O valor 9 foi digitado {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado!')
print(f'O(s) valore(s) pare(s) digitado(s): ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')