from time import sleep

def abrir_arquivo():
  try:
    arquivo = open('J:\\Desenvolvimento\\python-basico\\python-tryexcept\\teste2.txt', 'r')
    print(f'Arquivo aberto com sucesso!\nPath: {arquivo.name}')
  except FileNotFoundError as erro:
    print(f'ERRO! {erro}')
    opc = input('Deseja criar o arquivo? ').upper()
    if opc == 'SIM':
      try:
        criar_arquivo()
      except Exception as erro:
        return f'ERRO! {erro}'

def criar_arquivo():
  arquivo = open('J:\\Desenvolvimento\\python-basico\\python-tryexcept\\teste2.txt', 'w+')
  print(f'Arquivo criado com sucesso!\nPath: {arquivo.name}')


abrir_arquivo()

