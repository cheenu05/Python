# question one output guess

class A:
    x = 10

a1 = A() # 10
a2 = A() # 10

a1.x = 20 

print(a1.x) 
print(a2.x) 


# a1.x = 20 creates an instance variable for a1.
# a2 still refers to the class variable x = 10.