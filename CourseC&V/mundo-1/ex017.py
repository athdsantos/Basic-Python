'''catOposto = float(input('Cateto Oposto: '))
catAdj = float(input('Cateto Adjacente: '))
hi = (catOposto ** 2 + catAdj ** 2) ** (1/2)
print('Cat OP {} Cat Adj {} e hip {:.2f}'.format(catOposto, catAdj, hi))
'''
from math import hypot
catOposto = float(input('Cateto Oposto: '))
catAdj = float(input('Cateto Adjacente: '))
hi = hypot(catOposto, catAdj)
print('Cateto Oposto: {}\nCateto Adjacente: {}\nHipotenusa: {:.2f}'.format(catOposto, catAdj, hi))
