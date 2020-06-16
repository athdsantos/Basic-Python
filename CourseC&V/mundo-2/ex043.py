peso = float(input('Type your weight: '))
altura = float(input('Type your height: '))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print('Weight: {}\nHeight: {}\nIMC: {:.1f}\nCategory: UNDER WEIGHT!'.format(peso, altura, imc))
elif imc <= 25:
    print('Weight: {}\nHeight: {}\nIMC: {:.1f}\nCategory: IDEAL WEIGHT!'.format(peso, altura, imc))
elif imc <= 30:
    print('Weight: {}\nHeight: {}\nIMC: {:.1f}\nCategory: OVERWEIGHT!'.format(peso, altura, imc))
elif imc >= 40:
    print('Weight: {}\nHeight: {}\nIMC: {:.1f}\nCategory: MORBID OBESITY!'.format(peso, altura, imc))
else:
    print('Weight: {}\nHeight: {}\nIMC: {:.1f}\nCategory: OBESITY!'.format(peso, altura, imc))
