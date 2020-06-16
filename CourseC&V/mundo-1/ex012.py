price = float(input('How much is? R$'))
print('The product is R${:.2f}, but after 5% off is R${:.2f}'.format(price, price - (price*5/100)))