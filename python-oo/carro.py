from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, cor, marca, tanque, rodas=4):
      Veiculo.__init__(self, cor, marca, tanque, rodas)

    def abastecer(self, quantidade_litros):
      if self.tanque + quantidade_litros > 100:
        print(f'Quantidade de litros maior que a capacidade do tanque.')
      else:
        self.tanque += quantidade_litros
        print(f'Tanque abastecido com {quantidade_litros}.')
          