# 9️⃣ Find the largest number in a list without using max().

numbers = [3, 5, 2, 8, 1, 4]
large = numbers[0]

for i in numbers:
    if i > large:
        large = i

print(large)