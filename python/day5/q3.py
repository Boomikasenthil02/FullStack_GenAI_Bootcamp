#Q2 Given a list , find the smallest value 
numbers=[10,20.30,40,50]
smallest=numbers[0]
for i in numbers:
    if i<smallest:
       smallest=i
print("smallest =",smallest)