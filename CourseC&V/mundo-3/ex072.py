numeros = ('Zero', 'Um', 'Dois', 'Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
           'Onze','Doze','Treze','Catorze','Quinze','Dezessei','Dezessete','Dezoito','Dezenove','Vinte')

while True:
    escolha = int((input('Digite um número inteiro entre 0..20: ')))
    if 0 <= escolha <= 20:
        break
    print('Tente novamente.', end='')
print(numeros[escolha])
