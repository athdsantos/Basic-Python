class Person:
  def __init__(self, name, cpf, city, age):
    self.name = name
    self.cpf = cpf
    self.city = city
    self.age = age
  
  def __str__(self):
    return f'Name: {self.name}\nCPF: {self.cpf}\nCity: {self.city}\nIdade: {self.age}\n'
