number=[]
for i in range(5):
    value=int(input(f"Enter the number{i+1}:"))
    number.append(value)
    largest=number[0]
for n in number:
    if n> largest:
        largest=n
        print("largest number of the list =",largest)