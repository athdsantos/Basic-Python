from person import Person
from student import Student
from employee import Employee

person_student = Person('Python', 12312312345, 'Javalandia', 12)
print(person_student)
student1 = Student(person_student, 123)
print(student1)
person_student = Person('Java', 78978978990, 'Scriptlandia', 85)
employee1 = Employee(person_student, 123456, 'RH')
print(employee1)
