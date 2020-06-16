from math import sin, cos, tan, radians

angle = float(input('Type an angle: '))
seno = sin(radians(angle))
cosseno = cos(radians(angle))
tangente = tan(radians(angle))
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(seno, cosseno, tangente))
