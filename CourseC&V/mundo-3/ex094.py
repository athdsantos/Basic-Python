#lista cheia de dicionarios
dados = {'nome': '', 'sexo': '', 'idade': 0}
pessoas = []
totIdade = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F] ')).upper().strip()[0]
    while dados['sexo'] not in 'FfMm':
        dados['sexo'] = str(input('Valor incorreto! Sexo [M/F] ')).upper().strip()[0]
    dados['idade'] = int(input('Idade: '))
    totIdade += dados['idade']
    pessoas.append(dados.copy())
    dados.clear()
    r = str(input(f'Deseja continuar? [S/N] ')).upper().strip()[0]
    while r not in 'SsNn':
        r = str(input(f'Valor incorreto! Deseja continuar? [S/N] ')).upper().strip()[0]
    if r in 'Nn':
        break
print(f'Lista pessoas {pessoas}')
print('-=' * 30)
print(f'- O grupo tem {len(pessoas)} pessoas cadastradas!')
print(f'- A média de idade do grupo é de {totIdade / len(pessoas):.2f} anos')
print(f'- As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print(f'- A pessoas com idade superior a média de {totIdade / len(pessoas):.2f} anos foram: ', end='')
for p in pessoas:
    if p['idade'] >= totIdade / len(pessoas):
        print('      ')
        for k, v in p.items():
            print(f'{"":^5} {k} = {v}; ', end='')
        print()
print('PROGRAMA ENCERRADO')