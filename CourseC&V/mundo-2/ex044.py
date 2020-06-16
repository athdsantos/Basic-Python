valueProduct = float(input('Value of the product: R$'))
paymentCondition = int(input('Choose the form of payment\n'
                             '1 - In cash/Check (10% off)\n'
                             '2 - Card (5% off)\n'
                             '3 - Parceled out (2x in card)\n'
                             '4 - Parceled out (3x or more + 20% interest)\n'
                             '5 - Exit\nChoose the option: '))
if paymentCondition == 1:
    print('\n1 - In Cash/Check - 10% OFF\nTotal: R${:.2f}\n'.format(valueProduct - (valueProduct * 0.10)))
elif paymentCondition == 2:
    print('\n2 - Card - 5% OFF\nTotal: R${:.2f}\n'.format(valueProduct - (valueProduct * 0.05)))
elif paymentCondition == 3:
    print('\n3 - Parceled out - 2x in card\nTotal: R${:.2f}\nInstallments: 2x R${:.2f}'.format(valueProduct,
                                                                                               valueProduct / 2))
elif paymentCondition == 4:
    totalParcelas = int(input('How many parcelas? '))
    print('\n4 - Parceled out - {}x in card\nTotal: R${:.2f}\nInstallments: {}x R${:.2f}'.format(totalParcelas,
                                                                                                 valueProduct + (valueProduct * 0.2),
                                                                                                 totalParcelas,
                                                                                               (valueProduct + (valueProduct * 0.2)) / totalParcelas))
elif paymentCondition == 5:
    print('Thanks!')
    exit()
else:
    print('Option invalid, try again!')