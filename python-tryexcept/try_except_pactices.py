from time import sleep

def open_file():
  try:
    file = open('your_path', 'r')
    print(f'File opened with success!\nPath: {file.name}')
  except FileNotFoundError as error:
    print(f'ERROR! {error}')
    opt = input('Do you want create the file? ').upper()
    if opt == 'YES':
      try:
        create_file()
      except Exception as error:
        return f'ERROR! {error}'

def create_file():
  file = open('your_path', 'w+')
  print(f'File created with success!\nPath: {file.name}')


open_file()

