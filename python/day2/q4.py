age=int(input("Enter the age :"))
if age>=0 and age<=12:
    print("child")
elif age>=13 and age<=17:
    print("Teenager")
elif age>=18 and age<=59:
    print("adult")
elif age>=60:
    print("senior citizien")