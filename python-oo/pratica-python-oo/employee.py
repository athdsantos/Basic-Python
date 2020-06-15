from person import Person

class Employee:

  def __init__(self, person, id_employee, sector):
    self.person = person
    self.id_employee = id_employee
    self.sector = sector

  def __str__(self):
    return f'Employee: {self.person.name}\nID: {self.id_employee}\nSector: {self.sector}\Age: {self.person.age}\n'
