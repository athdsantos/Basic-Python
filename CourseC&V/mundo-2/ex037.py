from time import sleep

import os
number = int(input('Type a integer number: '))
choose = int(input('Choose an option\n1 - Binary\n2 - Octal\n3 - Hexadecimal\n4 - Sair\nOption: '))

if choose == 1:
    print('Conversion in progress...')
    sleep(2)
    print('The number {} in binary is {}.'.format(number, bin(number)[2:]))
elif choose == 2:
    print('Conversion in progress...')
    sleep(2)
    print('The number {} in octal is {}.'.format(number, oct(number)[2:]))
elif choose == 3:
    print('Conversion in progress...')
    sleep(2)
    print('The number {} in hexadecimal is {}.'.format(number, hex(number)[2:]))
elif choose == 4:
    print('Going out...Thanks for to use our program!')
    exit()
else:
    print('Invalid Option! Try again!')
