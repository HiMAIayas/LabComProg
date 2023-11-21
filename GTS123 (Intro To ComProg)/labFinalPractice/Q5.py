while True:
    size = int(input("Enter an integer number: "))
    if size==0:break
    if size<0 or size>9:
        print("Valid value is between 0 - 9")
        continue
    
    for i in range(size):
        print(" "*(size-i-1),end="")
        print(f"{size} "*(i+1))