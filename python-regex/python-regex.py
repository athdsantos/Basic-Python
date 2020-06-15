try:
  import re
  from requests import get
except Exception as erro:
  print(f'ERRO! {erro}')


def verificar_site(req=get('http://www.minasplatinum.com/pag.php?id=4')):
  try:
    if 200 >= req.status_code <= 299:
      buscar_emails()
    else:
      print('ERRO! Site indisponível no momento!')
  except Exception as erro:
    print(f'ERRO! {erro}')   


def buscar_emails(req=get('http://www.minasplatinum.com/pag.php?id=4')):
  try:
    padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', req.text)
    print('E-MAILS ENCONTRADOS:\n')
    for email in padrao:
      print(email, end='\n')
  except Exception as erro:
    print(f'ERRO! {erro}')


verificar_site()
