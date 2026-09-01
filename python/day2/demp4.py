age=18
age=int(input("Enter your age :"))
is_id= input("Do you have ID(Yes or No):")
if age >18:
    if is_id== "yes"or"YES" or "Yes":
        print("You are Eligible to vote")
    else:
        print("You need a id")
else:
    print("not eligible to vote")