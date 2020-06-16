number = int(input('Type a number: '))
print('Unit: {}\nTen: {}\nHundred: {}\nThousand: {}'.format((number // 1 % 10), (number // 10 % 10), (number // 100 % 10), (number // 1000 % 10)))
