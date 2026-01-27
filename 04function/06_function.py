# lets find the upcomming leap year 

def leap(year):
    if year % 4 == 0 and year % 100 == 0 and year % 400 != 0 :
        return (f"{year}. is not a Leap year")
    elif year % 4 == 0 :
        return (f"{year} is Leap year")
    else:
        return (f"{year} is not a leap year")
    
print(leap(2000))