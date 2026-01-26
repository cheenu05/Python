# 2️⃣ Function jo 3 numbers me se largest bataye

def largestValue(a,b,c):
      if a >= b and a >= c:
        return a
      elif b >= a and b >= c:
        return b
      else:
        return c
      
print(largestValue(10, 25, 15))
