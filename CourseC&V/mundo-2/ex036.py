from time import sleep

valueHouse = float(input('Value of house: R$'))
valuePayment = float(input('Value of your payment: R$'))
yearsBuy = float(input('Years of payment: '))

valueMonth = valueHouse / (yearsBuy * 12)

print('Processando as informações...')
sleep(2)

if valueMonth <= (valuePayment * 0.3):
    print('\nEmpréstimo aprovado!')
else:
    print('Empréstimo reprovado!')

print('\nValue House R${:.2f}\nPay: R${:.2f}\nYears of payment: {:.0f}\nValue of installments: R${:.2f}'.format(valueHouse,
                                                                                                          valuePayment,
                                                                                                          yearsBuy,
                                                                                                          valueMonth))