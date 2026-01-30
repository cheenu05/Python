# inheritance in python 
# Parent: User
# Child: Admin
# Method: login()
# Admin ka login different message de

class Parent:
    def __init__(self , name , lastname):
        self.name = name
        self.lastname = lastname
    def user(self):
        return f"{self.name} {self.lastname}"
    def login(self):
        print(f"Hello Mr.{self.name} {self.lastname}")
    
class Child(Parent):
    def __init__(self, name, lastname , admin_id):
        super().__init__(name, lastname)
        self.admin_id = admin_id   # child ka o
    def admin(self):
         return f"{self.name} {self.lastname} | Admin ID: {self.admin_id}"
    def login(self):
        print(f"Welcome Back admin {self.name} {self.lastname}")        


child1 = Child("Lakshya", "Malhotra", 2001)

print(child1.admin())
child1.login()


