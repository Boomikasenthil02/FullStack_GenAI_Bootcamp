unit=float(input("Enter the number:"))
if unit<=100 and unit>=0:
    cost=unit*2
    print("Cost=",cost)
elif unit>=101 and unit<=200:
    cost=unit*3
    print("Cost=",cost)
elif unit>=201 and unit<=300:
    cost=unit*5
    print("Cost=",cost)
elif unit>=300:
    cost=unit*7
    print("Cost=",cost)
else:
    print("Invaild unit")