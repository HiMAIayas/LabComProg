while True:
    n = int(input("Enter an integer number: "))
    if 1<=n<=10: break
    print("1 - 10 !!!")
    
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
    
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
    