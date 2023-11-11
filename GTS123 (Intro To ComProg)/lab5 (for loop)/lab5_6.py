for i in range(5):
    n=int(input("Enter a number between 1-20: "))
    if n<1 or n>20:print("Number is invalid")
    else:
        if n%2==0:print(f"{n} is even number")
        else:print(f"{n} is odd number")