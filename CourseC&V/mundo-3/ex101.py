def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    resultado = ano_atual - ano_nascimento
    print(f'Com {resultado} anos: ', end='')
    if resultado < 16:
        print('Não vota')
    elif resultado <= 16 & resultado < 18 or resultado >= 65:
        print('Voto opcional')
    else:
        print('Voto obrigatório')


while True:
    ano = int(input(f'Em que ano você nasceu? '))
    voto(ano)
