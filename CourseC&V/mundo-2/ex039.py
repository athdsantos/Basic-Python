import datetime
import time

dateBorn = int(input('Type your date of born (XXXX): '))
dateActual = datetime.date.today().year
age = dateActual - dateBorn
print('Processing..')
time.sleep(2)

if age < 18:
    print('{} years old, he is young, missing {} years!'.format(age, 18 - age))
elif age == 18:
    print('{} years old, it is time!!!'.format(age))
else:
    print('{} years old, you are late for enlistment, they passed {} years!'.format(age, age - 18))
