try:
  import re
  from requests import get
except Exception as error:
  print(f'ERROR! {error}')


def check_website(req=get('site_here')):
  try:
    if 200 >= req.status_code <= 299:
      fetch_emails()
    else:
      print('ERROR! Site is down!')
  except Exception as erro:
    print(f'ERROR! {error}')   


def fetch_emails(req=get('site_here')):
  try:
    pattern_email = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', req.text)
    print('E-MAILS FOUND!:\n')
    for email in pattern_email:
      print(email, end='\n')
  except Exception as error:
    print(f'ERROR! {error}')


check_website()
