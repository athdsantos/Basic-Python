name = input('Type your name: ').strip()
print('Your name is {}'.format(name))
print('Your name in upper is {}'.format(name.upper()))
print('Your name in lower is {}'.format(name.lower()))
print('Your name contain {} letters'.format(len(name) - name.count(' ')))
newName = name.split()
print('Your first name {}, contain {} letters.'.format(newName[0], len(newName[0])))