#. guess the output

class Counter:
    def __init__(self):
        self.count = 0

c1 = Counter()
c2 = Counter()

c1.count += 1
c2.count += 1
c2.count += 1

print(c1.count, c2.count)
