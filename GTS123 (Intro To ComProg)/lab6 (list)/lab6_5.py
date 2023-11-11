size = int(input("how many person in a group?: "))

a=[]
b=[]
c=[]
print("\nPlease enter a grade for group A")
for i in range(size): a.append(float(input("enter grade: ")))

print("\nPlease enter a grade for group B")
for i in range(size): b.append(float(input("enter grade: ")))

print("\nPlease enter a grade for group C")
for i in range(size): c.append(float(input("enter grade: ")))

print()
print(f"The highest grade in group A is {max(a)}")
print(f"The highest grade in group B is {max(b)}")
print(f"The highest grade in group C is {max(c)}")

