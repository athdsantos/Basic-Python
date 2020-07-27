import os

def createFoldersDevWeb():
  folder = input('Folder name: ')
  os.makedirs(f'your_path\{folder}\css')
  open(f'your_path\{folder}\css\style.css', '+w').close()
  os.makedirs(f'your_path\{folder}\js')
  os.makedirs(f'your_path\{folder}\images')
  open(f'your_path\{folder}\js\script.js', '+w').close()
  open(f'your_path\{folder}\index.html', '+w').close()
  os.chdir(f'your_path\{folder}')
  os.system(command='code .')


def createFoldersBasicPython():
  folder = input('Folder name: ')
  os.mkdir(f'your_path\{folder}')
  fileName = input('Type the file name: ')
  open(f'your_path\{folder}\{fileName}.py', '+w').close()
  os.chdir(f'your_path\{folder}')
  os.system(command='code .')


# Main code #

while True:
  try:
    print(f'{"-" * 15}Create structure{"-" * 15}\n')
    print('Choice the correct option below:\n1 - Project web development\n2 - Python folder and file\n3 - Exit\n')
    choice = int(input('Choice: '))
    if choice == 1:
      createFoldersDevWeb()
    elif choice == 2:
      createFoldersBasicPython()
    elif choice == 3:
      print('Program finished!')
      break
    else:
      print('Please, insert a value between 1 and 3!')
  except KeyboardInterrupt:
    print('App interrupted by user!')
    break
  except ValueError:
    print('Please, insert the correct value!')
  except Exception as error:
    print(f'{error}')