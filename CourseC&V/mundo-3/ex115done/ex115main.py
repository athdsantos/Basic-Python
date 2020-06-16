from Curso_em_video.ex115done.lib.interface import *
from Curso_em_video.ex115done.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        cabecalho('Cadastrar nova pessoa')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida!\033[m')
