class Veiculo:
  # Construtor
  def __init__(self, cor, marca, tanque, rodas):
    self.cor = cor
    self.rodas = rodas
    self.marca = marca
    self.tanque = tanque

  def abastecer(self, quantidade_litros):
      if self.tanque + quantidade_litros > 100:
        print(f'Quantidade de litros maior que a capacidade do tanque.')
      else:
        self.tanque += quantidade_litros
        print(f'Tanque abastecido com {quantidade_litros} litros.')

  def ficha_veiculo(self):
    print(f'\nCor do veículo: {self.cor}\nQuantidade de rodas: {self.rodas}\n'
          f'Marca: {self.marca}\nTanque: {self.tanque}L\n')