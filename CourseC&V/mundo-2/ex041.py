import datetime
import time
bornDate = int(input('Type your born date: '))
dateActual = datetime.date.today().year
age = dateActual - bornDate
print('Processing...')
time.sleep(2)

if age <= 9:
    print('You have {} years and your category is LITTLE.'.format(age))
elif age <= 14:
    print('You have {} years and your category is CHILDISH.'.format(age))
elif age <= 19:
    print('You have {} years and your category is JUNIOR.'.format(age))
elif age <= 25:
    print('You have {} years and your category is SENIOR.'.format(age))
else:
    print('You have {} years and your category is MASTER.'.format(age))