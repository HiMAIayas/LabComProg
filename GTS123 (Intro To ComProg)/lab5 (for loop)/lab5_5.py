n=int(input("Enter no. of lines: "))
if n<1:print("Error")
else:
    for i in range(1,n+1):
        if i%2==0:print("*"*i)
        else:print("-"*i)