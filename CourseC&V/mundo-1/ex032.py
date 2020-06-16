year = int(input('Type the year: '))
if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
    print('The year {} is leap!'.format(year))
else:
    print('The year {} is not leap'.format(year))
