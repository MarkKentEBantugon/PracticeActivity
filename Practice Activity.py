
class Person:
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        print('Person constructor')
        
class Student (Person):
    
    def __init__(self, name, age, student_id, sr_code):
        super().__init__(name, age)
        self.student_id = student_id
        self.sr_code = sr_code
        print('Student constructor')
        
        
student = Student('Mark Kent', 19, 107452080002, 2105936)
print(student.name)
print(student.student_id)
print(student.sr_code)
print(student.age)

person = Person('Kent', 20)
print(person.name)
print(person.age)