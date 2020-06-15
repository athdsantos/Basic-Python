from person import Person

class Student:

  def __init__(self, person, class_student):
    self.person = person
    self.class_student = class_student

  def __str__(self):
    return f'Student: {self.person.name}\nAge: {self.person.age}\Class: {self.class_student}\n'
