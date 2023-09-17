import math
a,b,c = input("Input: ").split("*")
opt = input("Please enter your choice (1,2): ")
if a.isnumeric() and b.isnumeric() and c.isnumeric():
    if int(a)>0 and int(b)>0 and int(c)>0:
        if opt=="1":
            print(f"The output is {int(a)+math.sqrt(int(b)**2+int(c)**3):.2f}")
        elif opt=="2":
            print(f"The output is {int(a+b)%int(c)}")
        else:print("Inalid input")
    else:print("Invalid input")
else:print("Invalid input")