from datetime import date
funcionario = {'nome': '', 'idade': 0, 'ctps': 0}
print('-=' * 25)
print(f'{"CADASTRO":^50}')
print('-=' * 25)
print()
funcionario['nome'] = str(input('Nome do funcionário: '))
funcionario['idade'] = int(input('Ano de nascimento: '))
anoNascimento = funcionario['idade']
idadeFunc = date.today().year - funcionario['idade']
funcionario['idade'] = idadeFunc
funcionario['ctps'] = int(input('Digite o nº da CTPS [0 em caso de não ter]: '))
if funcionario['ctps'] != 0:
    funcionarioCLT = {'anoContratacao': 0, 'salario': 0.0, 'contribuicao': 0}
    funcionarioCLT['anoContratacao'] = int(input('Ano de admissão: '))
    funcionarioCLT['salario'] = float(input('Salário: R$ '))
    aposentadoria = (funcionarioCLT['anoContratacao'] - anoNascimento) + 35
    funcionarioCLT['contribuicao'] = aposentadoria
    funcionario.update(funcionarioCLT)
    print()
    print('-=' * 25)
    print(f'{"RH":^50}')
    print('-=' * 25)
    print()
    for k, v in funcionario.items():
        print(f'A chave {k} tem o valor {v}')
else:
    print()
    print('-=' * 25)
    print(f'{"RH":^50}')
    print('-=' * 25)
    print()
    print(f'O funcionário não possui CTPS.')
    for k, v in funcionario.items():
        print(f'A chave {k} tem o valor {v}')
    exit()
