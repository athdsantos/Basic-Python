times = ('Cruzeiro', 'Náutico', 'Vitória', 'América Mineiro', 'Chapecoense', 'Avaí', 'Botafogo-SP', 'Brasil de Pelotas', 'Confiança', 'CRB', 'CSA', 'Cuiabá',
        'Figueirense',  'Guarani', 'Juventude',   'Oeste', 'Operário-PR', 'Paraná', 'Ponte Preta', 'Sampaio Corrêa')
print(f'Os 5 primeiros times da Série B 2020\n{times[0:5]}')
print(f'\nOs últimos 4 times da Série B 2020\n{times[-4:]}')
print(f'\nTimes da Série B 2020 em ordem alfabética\n{sorted(times)}')
print(f'\nO time da Chapecoense está na {times.index("Chapecoense") +1}º posição')