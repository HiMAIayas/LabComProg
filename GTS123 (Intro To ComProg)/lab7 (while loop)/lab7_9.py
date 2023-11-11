count=0
total=0
while True:
    n= int(input("Enter an integer (-1 to exit): "))
    if n==-1:
        break
    count+=1
    total+=n
    
print(f"The sum of {count} number(s) is {total}.")