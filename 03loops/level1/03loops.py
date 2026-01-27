#  3️⃣ Print the sum of numbers from 1 to n (n taken from user).

num = int(input("enter you number"))
total = 0

for i in range(1, num):
    total = total + i
    print(total)


# 🧠 Interview-Ready Explanation (Say this 👇)
    # “Since integers are not iterable in Python, we use range() to generate values.
    # Because range() excludes the stop value, we use range(1, n + 1) to include n while calculating the sum from 1 to n.”

