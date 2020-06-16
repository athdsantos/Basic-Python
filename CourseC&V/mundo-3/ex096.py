def calculaTerreno(larg, compr):
    area = larg * compr
    print(f'A área de um terreno {larg} x {compr} é de {area:.1f}m².')


print(f'{"Controle de Terrenos":^50}')
print('-' * 50)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
calculaTerreno(l, c)
