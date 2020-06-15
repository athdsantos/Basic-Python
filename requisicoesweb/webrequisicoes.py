import requests
from utils import *
#beatiful soup 4 bs4 pip3 install bs4

def menu():
  funcionalidade = ['Status', 'Headers', 'URL', 'History', 'Encodind', 'Reason', 'Cookies', 'Elapsed', 'Request']
  i = 1
  for c in funcionalidade:
    print(f'{i} - {c}')
    i += 1
  try:
    escolha = int(input('Escolha uma opção: '))
  except (ValueError, TypeError):
    return 'ERRO! Favor digitar um valor válido!'
  except:
    if escolha < 1 or escolha > 9:
      return 'ERRO! Favor digitar um valor válido!'

def site_user(user_site):
  titulo('verificação do site')
  #requisicao=requests.get(user_site)
  try:
    print(f'O site \033[32m{user_site}\033[m está funcionando corretamente!\n')
  except Exception as erro:
    print(f'ERRO! O site \033[31m{user_site}\033[m apresentou o erro: \033[1;33m{erro}\033[m')

def site_status(user_site):
  titulo('status code')
  requisicao = requests.get(user_site)
  print(f'Status code: {requisicao.status_code}\n')

def site_headers(user_site):
  titulo('headers')
  requisicao = requests.get(user_site)
  for chave, valor in requisicao.headers.items():
    print(f'{chave}: {valor}')

def site_url(user_site):
  titulo('url')
  requisicao = requests.get(user_site)
  print(f'URL: {requisicao.url}\n')

def site_history(user_site):
  titulo('history')
  requisicao = requests.get(user_site)
  print(f'History: {requisicao.history}\n')

def site_encoding(user_site):
  requisicao = requests.get(user_site)
  titulo('encoding')
  print(f'Encoding: {requisicao.encoding}\n')

def site_reason(user_site):
  requisicao = requests.get(user_site)
  titulo('reason')
  print(f'Reason: {requisicao.reason}\n')

def site_cookies(user_site):
  requisicao = requests.get(user_site)
  titulo('cookies')
  print(f'Cookies: {requisicao.cookies}\n')

def site_elapsed(user_site):
  requisicao = requests.get(user_site)
  titulo('elapsed')
  print(f'Elapsed: {requisicao.elapsed}\n')

def site_request(user_site):
  requisicao = requests.get(user_site)
  titulo('request')
  print(f'Request: {requisicao.request}\n')

while True:
  titulo('verificador de requests 1.0v')
  user_site = input('Digite o site que deseja avaliar: ')
  print()
  menu()


'''site_user(user_site)
site_status(user_site)
site_headers(user_site)
site_url(user_site)
site_history(user_site)
site_encoding(user_site)
site_reason(user_site)
site_cookies(user_site)
site_elapsed(user_site)
site_request(user_site)'''