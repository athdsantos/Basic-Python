from random import randint
vitorias = 0
while True:
    jogador = int(input('Digite um valor: '))
    pc = randint(0,10)
    total = pc + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print(f'Valor do usuário {jogador}; Valor do PC {pc}; Total de {total}')
    print(f'Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente!!')
print(f'Você venceu {vitorias} vezes!')
