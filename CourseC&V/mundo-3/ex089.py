alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA:>8"}')
print('-' * 26)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 30)
    opc = int(input('Mostrar as notas de qual aluno? [999 para sair]'))
    if opc == 999:
        break
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
print(f'\n{"OBRIGADO":^40}')
