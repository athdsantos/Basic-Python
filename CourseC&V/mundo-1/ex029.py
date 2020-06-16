velocity = int(input('Type the velocity: '))
if velocity <= 80:
    print('Congrats, your velocity is {}km/h and you are on the allowed!'.format(velocity))
else:
    print('That ugly, the limit is 80km/h and you are {}km/h above the allowed!'.format(velocity - 80))
    print('Your fine is R${:.2f}.'.format((velocity - 80) * 7))
