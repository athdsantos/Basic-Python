note1 = float(input('Type the first note: '))
note2 = float(input('Type the second note: '))

media = (note1 + note2) / 2

if media < 5:
    print('Your average is {:.1f} and you are DISAPPROVED!'.format(media))
elif media >= 5 and media <= 6.9:
    print('Your average is {:.1f} and you are in recuperation!'.format(media))
else:
    print('CONGRATS, your average is {:.1f} and you are APPROVED!!'.format(media))
