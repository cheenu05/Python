# Closure 

def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
        return x
    return inner

result = outer()
print(result()) # output => 1
print(result()) # output => 2
print(result()) # output => 3
print(result()) # output => 4
print(result()) # output => 5
print(result()) # output => 6

#  why this happens ? bcz

# “A closure in Python is a function that remembers variables from its enclosing scope even after the outer function has finished executing.
# Closures are created when a nested function uses variables from the outer function.
# They are commonly used for data hiding, state management, and decorators.”