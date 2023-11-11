a,b,c = input("a, b, c = ").split()
validList = ["True","False"]
if (a not in validList) or (b not in validList) or (c not in validList):
    print("Invalid input")
else:
    if a=="True" or (b == "False" and c=="False"):print("Grant")
    else: print("Deny")