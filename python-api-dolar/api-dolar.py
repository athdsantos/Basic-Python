from requests import get
from json import loads
from time import sleep

def get_requisicao():
  try:
    req = get('https://economia.awesomeapi.com.br/json/all/')
    if 200 >= req.status_code <= 299:
      return_information()
    else:
      print('ERRO! The site is down!')
  except Exception as erro:
    print(f'ERRO! {erro}')


def return_information():
  try:
    moeda_d = input('Moeda_d: ')
    moeda_r = input('Moeda_r: ')
    req = get('https://economia.awesomeapi.com.br/json/all/' + moeda_d + '-' + moeda_r)
    print('Buscando as informações..')
    sleep(2)
    for_dict = loads(req.text)
    print(f'Name: {for_dict["USD"]["name"]}')
    print(f'Code: {for_dict["USD"]["code"]}')
    print(f'Codein: {for_dict["USD"]["codein"]}')
    print(f'High value: R${for_dict["USD"]["high"]}')
    print(f'Low value: R${for_dict["USD"]["low"]}')
    print(f'Create date: {for_dict["USD"]["create_date"]}')
  except Exception as erro:
    print(f'ERRO! {erro}')

get_requisicao()
