# class and object 

class Students:
    def __init__(self, name , age):
        self.name = name
        self.age = age 
    def fullname(self):
        return f"{self.name} {self.age}"

student1 = Students("lakshya",24)
print(student1)
print(student1.fullname())

student2 = Students("Rohit" , 23)
print(student2.fullname())