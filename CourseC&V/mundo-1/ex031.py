distance = int(input('Type the distance in km: '))
if distance <= 200:
    print('Your distance is {}km and your passage is R${:.2f}.'.format(distance, distance * 0.5))
else:
    print('Your distance is {}km and your passage is R${:.2f}.'.format(distance, distance * 0.45))
