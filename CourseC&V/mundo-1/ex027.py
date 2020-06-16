name = input('Type your full name: ').strip()
newName = name.split()
print('Your full name is {}, the first name is {} and the last name is {}.'.format(name, newName[0], newName[len(newName) - 1]))
