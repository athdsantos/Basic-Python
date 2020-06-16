from time import sleep
import emoji

contagem = 10
print('Contagem regressiva para os fogos em...')
for c in range(contagem, -1, - 1):
    print('{} segundos..'.format(contagem))
    sleep(1)
    contagem -= 1
print(emoji.emojize(':fireworks:' * 10))
