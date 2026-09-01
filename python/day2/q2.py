mark=int(input("Enter your mark :"))
if mark>=90 and mark<=100:
    print("Your grade is A")
elif mark>=80 and mark<=89:
    print("Your grade is B")
elif mark>=70 and mark<=79:
    print("Your grade is C")
elif mark>=60 and mark<=69:
    print("Your grade is D")
elif mark>=0 and mark<=59:
    print("Your Score is low")
else:
    print("Enter the valid number")