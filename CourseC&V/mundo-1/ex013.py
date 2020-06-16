payment = float(input('How much is your payment? '))
print('Your payment this month was R${:.2f}, but with increase of 15%, go to R${:.2f}.'.format(payment, payment + (payment*0.15)))
