larg = float(input('How much is the width? '))
alt = float(input('How much is the height? '))
print('You have an area of {:.1f}x{:.1f} and you need to buy {:.1f}l of ink.'.format(larg, alt, (alt * larg) / 2))
