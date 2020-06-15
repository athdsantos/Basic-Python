from person import Person

class Student:

  def __init__(self, person, class):
    self.person = person
    self.class = class

  def __str__(self):
    return f'Student: {self.person.name}\nAge: {self.person.age}\Class: {self.class}\n'
