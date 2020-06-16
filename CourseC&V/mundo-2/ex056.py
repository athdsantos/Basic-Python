somaIdade = 0
idadeHomem = 0
nomeHomemold = ''
totMulher20 = 0
for c in range(1, 5):
    nome = input('Qual seu nome? ').strip()
    idade = int(input('Qual sua idade? '))
    sexo = input('Qual o sexo? ').strip()
    somaIdade += idade
    if c == 1 and sexo in 'Mm':
        idadeHomem += idade
        nomeHomemold += nome
    if sexo in 'Mm' and idade > idadeHomem:
        idadeHomem = idade
        nomeHomemold = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1
print('A média de idade entre as 4 pessoas é de {:.1f} anos.'.format((somaIdade / 4)))
print('Homem mais velho {}, tem {} anos.'.format(nomeHomemold, idadeHomem))
print('{} mulhere tem mais que 20 anos.'.format(totMulher20))
