year = int(input("Enter a year : "))
 
if year % 100 == 0:
    if year % 400 == 0:
        print(year, "is leap year.")
    else:
        print(year + 4, "is next leap year")
elif year % 4 == 0:
    print(year, "is leap year")
else:
    next_year = year % 4 
    print(year + next_year, "is next leap year")