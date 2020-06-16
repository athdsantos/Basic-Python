payment = float(input('Type your payment: R$'))

if payment >= 1250:
    print('Your payment now is R${:.2f}.'.format(payment * 0.10 + payment))
else:
    print('Your payment now is R${:.2f}.'.format(payment * 0.15 + payment))
