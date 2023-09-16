a =float(input("a = "))
b =float(input("b = "))
c =float(input("c = "))

if a>0 and b>0 and c>0 and max(a,b,c) < a+b+c-max(a,b,c):print("Form a triangle")
else:print("Not form a triangle")
