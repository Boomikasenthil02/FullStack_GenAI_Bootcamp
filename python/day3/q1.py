# Digit Counting 
number =int(input("Enter the number:"))
count=0
while number>0:
    number=number//10
    count=count+1
print("Total number of counting is :",count)