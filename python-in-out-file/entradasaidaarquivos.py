arquivo = open('your_path', 'r+')
try:
  file.read()
except:
  file.write()

for row in file:
  if row == 'python':
    

for c in range(3):
  name = input('Name: ')
  age = input('Age: ')
  file.write(name)
  file.write('\t\t\t')
  file.write(age)
  file.write('\n')'''

