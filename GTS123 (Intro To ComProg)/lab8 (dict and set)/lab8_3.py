l1=[int(i) for i in input("Input sequence1: ").split() if i.isnumeric() ]
l2=[int(i) for i in input("Input sequence2: ").split() if i.isnumeric() ]

if set(l1)==set(l2):print("same set")
else:print("different set")

print(l1,l2)
print(set(l1))
print(set(l2))