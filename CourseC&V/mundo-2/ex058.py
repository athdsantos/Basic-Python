from random import randint

pc = 0
contTentativas = 1

usuario = int(input('Tente adivinhar o número do PC: '))

while pc != usuario:
    print('ERRRRROUUU!')
    pc = randint(0, 10)
    contTentativas += 1
    usuario = int(input('\nTente novamente: \n'))
print('\nACERTOUUUU!\nNúmero do PC {}'.format(pc))
print('Número do usuário {}\n'.format(usuario))
print('Palpites necessários: {}'.format(contTentativas))
