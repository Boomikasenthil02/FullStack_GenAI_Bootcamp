#separate even and odd 
numbers=[1,2,3,4,5,6,7,8]
even=[]
odd=[]
for i in numbers:
    if i%2==0 :
        even.append(i)
    else:
        odd.append(i)
print("Even number is:",even)
print("odd number is :",odd)
