from vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, color, brand, tank, wheels=4):
      Vehicle.__init__(self, color, brand, tank, wheels)

    def to_fuel(self, quantity_liters):
      if self.tank + quantity_liters > 100:
        print(f'Number of liters greater than the tank.')
      else:
        self.tank += quantity_liters
        print(f'Fueled tank {quantity_liters}.')
          
