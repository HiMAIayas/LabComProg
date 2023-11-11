n=int(input("Enter an integer number (n>0): "))
op=input("(1) Factorial of n (n!)\n(2) Summation of n integers\nSelect operation: ")
print()
if n<=0 or (op!="1" and op!="2"):print("N/A Operation!")
else:
    if op=="1":
        ans=1
        for i in range(1,n+1):ans*=i
        print(f"Factorial of n (n!) = {ans}")
    elif op=="2":
        ans=0
        for i in range(n+1):ans+=i
        print(f"Summation of n integers = {ans}")