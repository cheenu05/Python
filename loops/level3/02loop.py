# 1️⃣2️⃣ Count how many vowels are in a string.

word = input("enter your word => ")
count = 0
for i in word:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count = count + 1
        
print(count)

