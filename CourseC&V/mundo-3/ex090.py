aula = {}
print('-=' * 25)
print(f'{"SITUAÇÃO FINAL":^50}')
print('-=' * 25)
print()
aula['nome'] = str(input('Nome do aluno: '))
aula['media'] = float(input(f'Média de {aula["nome"]}: '))
print()
if aula['media'] >= 7:
    aula['situação'] = 'APROVADO'
    print(f'Aluno(a) {aula["nome"]} teve média de {aula["media"]} e sua situação é {aula["situação"]}')
elif aula['media'] <= 4.5:
    aula['situação'] = 'REPROVADO'
    print(f'Aluno(a) {aula["nome"]} teve média de {aula["media"]} e sua situação é {aula["situação"]}')
else:
    aula['situação'] = 'RECUPERAÇÃO'
    print(f'Aluno(a) {aula["nome"]} teve média de {aula["media"]} e sua situação é {aula["situação"]}')
