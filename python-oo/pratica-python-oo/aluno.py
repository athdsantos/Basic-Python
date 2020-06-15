from pessoa import Pessoa

class Aluno:

  def __init__(self, pessoa, turma):
    self.pessoa = pessoa
    self.turma = turma

  def __str__(self):
    return f'Aluno: {self.pessoa.nome}\nIdade: {self.pessoa.idade}\nTurma: {self.turma}\n'