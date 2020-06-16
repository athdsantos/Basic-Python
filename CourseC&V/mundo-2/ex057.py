sexo = input('Qual seu sexo? ').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Valor incorreto! Digite seu sexo [F/M]: ').strip().upper()[0]
if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino!'
print('Correto, você é do gênero {}'.format(sexo))
