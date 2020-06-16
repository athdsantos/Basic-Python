from random import choice

name1 = input('Type the first student: ')
name2 = input('Type the second student: ')
name3 = input('Type the third student: ')
name4 = input('Type the fourth student: ')

listOfStudents = [name1, name2, name3, name4]

draw = choice(listOfStudents)

print('The name chosen was {}!!'.format(draw))
