number1 = int(input('Type a number: '))
number2 = int(input('Type other number: '))

if number1 > number2:
    print('The first number typed {} is bigger than the second {}.'.format(number1, number2))
elif number2 > number1:
    print('The second number typed {} is bigger than the first {}.'.format(number2, number1))
else:
    print('The two numbers {} and {} are equals.'.format(number1, number2))
