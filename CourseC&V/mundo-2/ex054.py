from datetime import date
menor = 0
maior = 0
dateAtual = date.today().year
for c in range(1, 8):
    data = int(input('Qual sua data de nascimento? '))
    if dateAtual - data >= 21:
        print('Maior ', dateAtual - data)
        maior += 1
    else:
        print('Menor ',dateAtual - data)
        menor += 1
print('{} pessoas são maiores de idade\n{} são menores de idade'.format(maior, menor))
