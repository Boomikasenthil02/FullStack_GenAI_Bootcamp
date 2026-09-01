year=int(input("Enter the year:"))
if year%400==0:
    print("This is the leap year")
elif year%100==0:
    print("This is the not leap year")
elif year %4==0:
    print("This is the leap year")
else:
    print("not a leap year")