number1 = int(input('Type a number: '))
number2 = int(input('Type other number: '))
number3 = int(input('Type other number: '))

if number1 < number2 < number3:
    print('The number {} it is bigger!'.format(number3))
elif number3 < number2 < number1:
    print('The number {} it is bigger!'.format(number1))
else:
    print('The number {} it is bigger!'.format(number2))
