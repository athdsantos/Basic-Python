dados = []
listaFinal = []
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(listaFinal) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    listaFinal.append(dados[:])
    dados.clear()

    r = str(input('Deseja continuar [S/N]? '))
    if r in 'Nn':
        break

print(f'Lista final com {len(listaFinal)} pessoas cadastradas.')
print(f'O maior peso foi {mai}kg. Peso de ', end='')
for l in listaFinal:
    if l[1] == mai:
        print([l[0]], end=' ')
print()
print(f'\nO menor peso foi {men}kg. Peso de ', end='')
for l in listaFinal:
    if l[1] == men:
        print([l[0]], end=' ')
