from pessoa import Pessoa
from aluno import Aluno
from funcionario import Funcionario

pessoa_aluno = Pessoa('Python', 12312312345, 'Javalandia', 12)
print(pessoa_aluno)
aluno1 = Aluno(pessoa_aluno, 123)
print(aluno1)
pessoa_funcionario = Pessoa('Java', 78978978990, 'Scriptlandia', 85)
funcionario1 = Funcionario(pessoa_funcionario, 123456, 'RH')
print(funcionario1)