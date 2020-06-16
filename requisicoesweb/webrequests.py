import requests
from utils import *

def menu():
  functionality = ['Status', 'Headers', 'URL', 'History', 'Encodind', 'Reason', 'Cookies', 'Elapsed', 'Request']
  i = 1
  for c in functionality:
    print(f'{i} - {c}')
    i += 1
  try:
    choice = int(input('Choice an option: '))
  except (ValueError, TypeError):
    return 'ERROR! Please, type a correct value!'
  except:
    if choice < 1 or choice > 9:
      return 'ERROR! Please, type a correct value!'

def site_user(user_site):
  title('Verification of website')
  try:
    print(f'The website \033[32m{user_site}\033[m is functioning correctly!\n')
  except Exception as error:
    print(f'ERROR! The website \033[31m{user_site}\033[m is the error: \033[1;33m{error}\033[m')

def site_status(user_site):
  title('status code')
  req = requests.get(user_site)
  print(f'Status code: {requisicao.status_code}\n')

def site_headers(user_site):
  title('headers')
  req = requests.get(user_site)
  for key, value in req.headers.items():
    print(f'{key}: {value}')

def site_url(user_site):
  title('url')
  req = requests.get(user_site)
  print(f'URL: {requisicao.url}\n')

def site_history(user_site):
  title('history')
  req = requests.get(user_site)
  print(f'History: {req.history}\n')

def site_encoding(user_site):
  req = requests.get(user_site)
  title('encoding')
  print(f'Encoding: {req.encoding}\n')

def site_reason(user_site):
  req = requests.get(user_site)
  title('reason')
  print(f'Reason: {req.reason}\n')

def site_cookies(user_site):
  req = requests.get(user_site)
  title('cookies')
  print(f'Cookies: {req.cookies}\n')

def site_elapsed(user_site):
  req = requests.get(user_site)
  title('elapsed')
  print(f'Elapsed: {req.elapsed}\n')

def site_request(user_site):
  req = requests.get(user_site)
  title('request')
  print(f'Request: {req.request}\n')

while True:
  title('Requisition Checker 1.0v')
  user_site = input('Type the webiste: ')
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
