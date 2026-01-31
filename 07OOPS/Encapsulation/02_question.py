# ❓ Question 1 (Easy → Realistic)

# Ek class banao User:
# Requirements:
# • Private variable: __age
# • Constructor me age set karo
# • Method get_age() → age return kare
# • Method set_age(age):
# • age < 18 ho → "Not allowed"
# • age ≥ 18 ho → age update ho jaye
# Rules:
# • __age ko direct access nahi karna
# • Sirf methods ke through kaam ho
# 👉 Tu:
# Class likh
# Object bana
# set_age() + get_age() test kar

class User:
    def __init__(self):
        self.__age = 0
    
    def set_age(self, age):
        if age < 18 :
            print("Not allowed")
        elif age >= 18 :
            self.__age = age

    def get_age(self):
        return f" Your age is = {self.__age}"
    
    
user1 = User()

user1.set_age(24)
print(user1.get_age())

print(user1.__age) # error ayeaa  [remove this line for valid result]



# user1.__age   ❌
# user1._User__age   ✅ (but SHOULD NOT use)