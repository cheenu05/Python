# is this code vaild or not 
# if it is valid then why ?

class Test:
    def show(self):
        print("Hello")

t = Test()
Test.show(t)


# Yes, the code is valid because self is just a reference to the object.
# When we call Test.show(t), we are manually passing the object t as self.