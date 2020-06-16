import requests
from time import sleep
while True:
    try:
        requests.get('http://pudim.com.br/')
        sleep(1)
    except KeyboardInterrupt:
        print(f'\033[1;91mExecução interrompida pelo usuário.')
        break
    except:
        sleep(1)
        print(f'\033[1;31mO site pudim não está acessível no momento!')
    else:
        sleep(1)
        print(f'\033[1;32mO site pudim está acessível no momento!')
