from pessoa import Pessoa

class Funcionario:

  def __init__(self, pessoa, id_funcionario, setor):
    self.pessoa = pessoa
    self.id_funcionario = id_funcionario
    self.setor = setor

  def __str__(self):
    return f'Funcionário: {self.pessoa.nome}\nID: {self.id_funcionario}\nSetor: {self.setor}\nIdade: {self.pessoa.idade}\n'