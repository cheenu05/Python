# Why is self required in class methods?

class Students:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def fullname(self):
        return f"{self.name},{self.age}"        


student1 = Students("lakshya", 24)
student2 = Students("rohit", 23)

print(student1.fullname())
print(student2.fullname())

# self is required for storing the value of object and without self we couldn't connect with obj

#  “self is required to refer to the current object.
# It allows instance methods to access and modify object-specific data.”