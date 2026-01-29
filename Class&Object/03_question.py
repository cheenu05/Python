# guess the output

class Student:
    def __init__(self, name):
        self.name = name

s = Student("Lakshya")
print(s.__dict__) # it is used to create dictionary {key : value}


# Interview-level explanation:

# The bug is that name = name does not store data in the object.
# We must use self.name = name to save it as an instance variable.