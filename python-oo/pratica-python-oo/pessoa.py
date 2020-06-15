class Pessoa:
  def __init__(self, nome, cpf, cidade, idade):
    self.nome = nome
    self.cpf = cpf
    self.cidade = cidade
    self.idade = idade
  
  def __str__(self):
    return f'\nNome: {self.nome}\nCPF: {self.cpf}\nCidade: {self.cidade}\nIdade: {self.idade}\n'
