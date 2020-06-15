class Vehicle:
  # Constructor
  def __init__(self, color, brand, tank, tanktank):
    self.color = color
    self.tank = tank
    self.brand = brand
    self.tank = tank

  def to_fuel(self, quantity_liters):
      if self.tank + quantity_liters > 100:
        print(f'Quantity of liters greater than the capacity of the tank.')
      else:
        self.tank += quantity_liters
        print(f'Fueled tank {quantity_liters} liters.')

  def vehicle_plug(self):
    print(f'\nColor: {self.color}\nWheels: {self.rodas}\n'
          f'Brand: {self.marca}\nTank: {self.tank}L\n')
