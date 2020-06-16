'''
============Fatiamento==========

#mostra a letra que está na posição 9
print(frase[9])

#mostra o intervalo de x..y
print(frase[9:21])

#mostra letras de x..y pulando de 2 em 2
print(frase[9:21:2])

#mostra desde o inicio, posição 0
print(frase[:5])

#mostra a partir da posição 15 sem saber o final
print(frase[15:])

#mostra letras de x ao final pulando de 3 em 3
print(frase[9::3])

============Análise==========

#contagem de caracteres na string
print(len(frase))

#contagem de quantas vezes a letra 'o' aparece
print(frase.count('o'))

#fatia e frase e realiza a contagem; 'letra',posição incial, posição final
print(frase.count('o',0,13))

#procura a 'palavra', onde inicia a 'palavra'
print(frase.find('deo'))

#se existe mostra a posição que inicia, senão -1 (falso)
print(frase.find('Pithon'))
print(frase.find('Python'))

#se existe 'True', senão, 'False'
print('Curso' in frase)
print('Cursu' in frase)

============Transformação==========

# Muda o 'Python' por 'Android'
print('\n', '=' * 20,'Replace', '=' * 20)
print('Normal phrase: {}.'.format(frase))
newPhrase = frase.replace('Python', 'Android')
print('New phrase after change "Python to Android".\n', newPhrase, '\n')

# Deixa tudo em maiúsculo
print('=' * 20, 'Upper', '=' * 20)
print('Normal phrase: {}.'.format(frase))
print('Phrase all in upper.\n', frase.upper(), '\n')

# Deixa tudo em minúsculo
print('=' * 20, 'Lower', '=' * 20)
print('Normal phrase: {}.'.format(frase))
print('Phrase all in upper.\n', frase.lower(), '\n')

# somente o primeiro caractere em maiusculo
print('=' * 20, 'Capitalize', '=' * 20)
print('Normal phrase: {}.'.format(frase))
print('Phrase after capitalize:\n', frase.capitalize(), '\n')

# Palavra por palavra a primeira letra maisucula
print('=' * 20, 'Title', '=' * 20)
print('Normal phrase: {}.'.format(frase))
print('Before title:\n',frase.title(),'\n')

# remover espaços excedentes
print('=' * 20, 'Strip', '=' * 20)
frase3 = '   Curso em Video Python  '
print('Length phrase before strip: ',len(frase3))
newPrhase3 = frase3.strip()
print('Length phrase before strip: ',len(newPrhase3), '\n')

# remove apenas os epaços da direita
print('=' * 20, 'RStrip', '=' * 20)
print('Length phrase before rstrip: ',len(frase3))
newPrhase4 = frase3.rstrip()
print('Length phrase after rstrip (remove spaces of right): ',len(newPrhase4), '\n')

# remove apenas os epaços da esquerda
print('=' * 20, 'LStrip', '=' * 20)
print('Length phrase before lstrip: ',len(frase3))
newPrhase5 = frase3.lstrip()
print('Length phrase after lstrip (remove spaces of left): ',len(newPrhase5), '\n')

============Divisão==========

# divide a frase em palavras, gerando um novo vetor
print('Normal Phrase: {}'.format(frase))
print('New Phrase after split:\n{}.'.format(frase.split()))

============Junção==========

frase = 'Curso em Video Python'
newPhrase = frase.split()
print('Antes da junção {};\nApós a junção {}'.format(frase, '-'.join(newPhrase)))

=======================================FOR==========================================

for c in range(1, 7):
    print(c)
print('Fim')

for c in range(7, 0, -1):
    print(c)
print('Fim')

for c in range(0, 7, 2):
    print(c)
print('Fim')

n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('Fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM!')

s = 0
for c in range(0,4):
    n = int(input('Digite um número: '))
    s += n
print('Fim! {}'.format(s))


num = 1
while num != 0:
    num = int(input('Digite um valor, só vamos parar quando apertar 0: '))
print('FIM')

n = 1
numPar = 0
numImpar = 0

while n != 0:
    n = int(input('Digite um valor (0 para parar): '))
    if n% 2 ==0:
        numPar += 1
    else:
        numImpar += 1
print('Você digitou {} números ímpares e {} pares!'.format(numImpar, numPar))

num = 1
numImpar = []
numPar = []
res = 'S'
while res == 'S':
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        numPar.append(num)
    else:
        numImpar.append(num)
    res = input('Deseja continuar? [S/N]').upper()
print('Total de valores pares: {}'.format(len(numPar)))
print('Valores pares: {}'.format(numPar))
print('Total de valores ímpares: {}'.format(len(numImpar)))
print('Valores pares: {}'.format(numImpar))

nome = 'Python'
idade = 23
aniversario = 10
print(f'Olá {nome}, o sr. tem {idade + aniversario} anos!')


lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for c in lanche:
    print(f'Eu vou comer {c}')

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for c in range(0, len(lanche)):
    print(c, lanche[c])

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for c, pos in enumerate(lanche):
    print(c, pos)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(f'Tupla "A" {a}\nTupla "B" {b}\nTuplas "A" e "B" {c}\nTuplas "A" e "B" ordenadas {sorted(c)}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(f'Contagem {c.count(5)}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(5))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(5, 1))

pessoa = ('Python', 23, 'M', 70.0)
del(pessoa)
print(pessoa)



nomes = []
n = str(input('Digite seu nome: '))
nomes.append(n)
print(nomes)






nomes = []
n = str(input('Digite seu nome: '))
nomes.append(n)
print(nomes)
n = str(input('Digite seu nome: '))
nomes.insert(0, n)
print(nomes)




nomes = ['Python', 'Java', 'C#', 'Cobol', 'JS']
print(f'Lista {nomes}')
del nomes[3]
print(f'Removendo o índice 3 através do del {nomes}')
nomes.pop(3)
print(f'Removendo através do Pop {nomes}')






nomes = ['Python', 'Java', 'C#', 'Cobol', 'JS']
nomes.remove('valor')






nomes = ['Python', 'Java', 'C#', 'Cobol', 'JS']
print(f'\nLista {nomes}\n')
del nomes[3]
print(f'Removendo o índice 3 através do del {nomes}\n')
nomes.pop(3)
print(f'Removendo através do Pop {nomes}\n')
if 'Java' not in nomes:
    print('O valor não existe!\n')
else:
    print(f'Valor {nomes.remove("Java")} foi removido com sucesso!')





valores = list(range(4, 11))
print(valores)







valores = list(range(4, 11, 2))
print(valores)






valores = ['Python', 'Java', 'C#', 'Cobol', 'JS']
print(valores)
valores.sort()
print(valores)



valores = ['Python', 'Java', 'C#', 'Cobol', 'JS']
print(f'Valores normais {valores}')
valores.sort()
print(f'Valores ordenados {valores}')
valores.sort(reverse=True)
print(f'Valores em ordem decrescente {valores}')





valores = ['Python', 'Java', 'C#', 'Cobol', 'JS']
print(f'Tamanho {len(valores)}')





valores = []
valores.append(5)
valores.append(4)
valores.append(9)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('FIM')







valores = []
for cont in range(6):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('FIM')




a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'A: {a}')
print(f'B: {b}')




pessoas = [['Python', 25], ['Java', 19], ['JS', 32]]
print(pessoas[0][0])
print(pessoas[1])




teste = []
teste.append('Python')
teste.append(23)
galera = []
galera.append(teste[:])
teste[0] = 'Java'
teste[1] = 10
galera.append(teste[:])
print(galera)


galera = [['Python', 25], ['Java', 19], ['JS', 32]]
for g in galera:
    print(f'Mostrar dados completos: {g}\n')
    #print(f'Mostrar apenas os nomes: {g[0]}\n')
    #print(f'Mostrar apenas idades: {g[1]}')






dado = []
galera = []
totMaior = totMenor = 0
for c in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for g in galera:
    if g[1] >= 21:
        print(f'{g[0]} é maior da idade com {g[1]} anos!')
        totMaior += 1
    else:
        print(f'{g[0]} é menor de idade com {g[1]} anos!')
        totMenor += 1
print(f'Temos no total {totMenor} pessoas menores de idade e {totMaior} pessoas maiores de idade')





dados = {'nome': 'Python', 'idade': 25, 'sexo': 'M'}



filmes = {'titulo': 'Harry Potter', 'ano': 2001, 'genero': 'Ação'}
print(f'Values: {filmes.values()}')
print(f'Keys: {filmes.keys()}')
print(f'Item: {filmes.items()}')






pessoas = {'nome': 'Python', 'sexo': 'M', 'idade': 23}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e é do sexo {pessoas["sexo"]}')
del pessoas["sexo"]
print(f'{pessoas.keys()}')
print(f'O del apaga a chave e o valor')








filmes = {'titulo': 'Harry Potter', 'ano': 2001, 'genero': 'Ação'}
for k, v in filmes.items():
    print(f'O {k} é {v}')

#### k é a key e o v são os valores

# Resultado

O titulo é Harry Potter
O ano é 2001
O genero é Ação






pessoas = {'nome': 'Python', 'sexo': 'M', 'idade': 23}
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['nome'] = 'Javascritp'
print(f'\nApós alterar "nome"...\n')
for k, v in pessoas.items():
    print(f'{k} = {v}')









#criado uma lista
brasil = []

#criando dois dicionários
estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}


#adicionando valores do dict dentro da lista brasil
brasil.append(estado1)
brasil.append(estado2)

#mostrando a lista Brasil, onde irá mostrar os dicionários estados 1 e 2 dentro da lista Brasil
print(brasil)

#mostrando cada dicionário estados 1 e 2
print(estado1)
print(estado2)




#criado uma lista
brasil = []

#criando dois dicionários
estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}


#adicionando valores do dict dentro da lista brasil
brasil.append(estado1)
brasil.append(estado2)

#mostrando o indice 1 da lista brasil e o valor 'sigla' do dicionário
print(f'{brasil[1]["sigla"]}')

#mostrando o indice 0 da lista brasil e o valor 'uf' do dicionário
print(brasil[0]['uf'])




estado = dict()
brasil = list()
for c in range(2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
# for de fora é da lista, percorre normalmente // for de dentro é dos dicts, percorre key e value através do 'b' que é a lista
for b in brasil:
    # percorre a chave e o valor
    for k, v in b.items():
      print(f'O campo {k} tem valor {v}')
print()
#percorre somente o valor
for b in brasil:
    for v in b.values():
        print(f'{v}', end=' ')
    print()


def mostraLinha(texto):
    print('-' * 50)
    print(f'{texto:^50}')
    print('-' * 50)

mostraLinha('Curso de Python')
mostraLinha('Curso em Vídeo')






def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma entre {a} e {b} é igual a {s}')


soma(b=2, a=5)







def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIMM')

contador(1)
contador(5, 2, 9, 3)
contador(2, 9)





def soma(a, b):
    s = a + b
    print(f'A soma entre {a} e {b} é igual a {s}')


soma(2, 5)












def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [2 ,5, 6, 9, 8]
print(valores)
dobra(valores)
print(valores)




def contaador(i, f, p):
    """
    Contagem e mostra na tela
    :param i: início da contagem
    :param f: final da contagem
    :param p: de quanto em quanto irá pular
    :return: no return
    """
    c = i
    if i > f:
        while c >= f:
            print(f'{c}', end='...')
            c -= p
    if i < f:
        while c <= f:
            print(f'{c}', end='...')
            c += p

help(contaador)



def soma_opcional(a=0, b=0, c=0):
    s = a + b + c
    print(s)


soma_opcional(5)


def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(5, 8, 6)
r2 = soma(2, 9)
r3 = soma(9)
print(f'Os resultado deram {r1}, {r2}, {r3}')

'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Erro de valores, favor inserir um valor correto para o numerador!')
except ZeroDivisionError:
    print('Não é possível dividir o número por 0!')
except KeyboardInterrupt:
    print('O usuário interrompeu a execução do programa!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre!')