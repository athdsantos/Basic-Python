from vehicle import Vehicle
from car import Car

vehicle1 = Vehicle('Black','Ford', 10, 2)
vehicle1.vehicle_plug()
vehicle1.to_fuel(25)
vehicle1.vehicle_plug()
vehicle2 = Vehicle('Silver', 'FIAT', 15, 3)
vehicle2.vehicle_plug()
vehicle2.to_fuel(65)
vehicle2.vehicle_plug()
car1 = Car('Red', 'Honda', 50)
car1.vehicle_plug()
car1.to_fuel(51)
car1.vehicle_plug()
