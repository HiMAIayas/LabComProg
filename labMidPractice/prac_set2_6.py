import math
a,b = input("Enter two integers: ").split()
if a.isnumeric() and b.isnumeric():
    a,b = int(a),int(b)
    if 1<a<30 and 1<b<30:
        
        ans = math.sqrt(sum([i for i in range(min(a,b),max(a,b)+1)]))
        print(f"Minimum number is {min(a,b)}")
        print(f"Maximum number is {max(a,b)}")
        print(f"The square root of the summation is {ans:.2f}")
            
    else:print("Invalid input")
else:print("Invalid input")