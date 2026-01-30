# ✅ Q1: Basic Inheritance
# Ek class banao:
# Person
# attributes: name, age
# method: introduce() → "Hi, I am <name> and I am <age> years old"
# Student (inherits Person)
# extra attribute: roll_no
# method: study() → "Student is studying"
# 👉 Task:
# Student ka object bana
# introduce() aur study() dono call karo

class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi , I am {self.name} and I am {self.age} years old"
    
class Students(Person):
    def __init__(self, name, age , roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no
    
    def study(self):
        return f"{self.name} is studying"


student1 = Students("lakshya" , 24 , 16)
print(student1.introduce())
print(student1.study())