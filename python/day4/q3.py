def find_largest(a,b,c):
    if a>b and b>c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c 
result=find_largest(20,30,40)
print("largest=",result)