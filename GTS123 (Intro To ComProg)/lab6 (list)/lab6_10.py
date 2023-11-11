fruitList=["Apple","Banana","Orange","Grape","Mango","Kiwi"]

print("List of fruits:",fruitList)
for i in fruitList:
    if len(i)>=6:
        print(f"\t{i} is 6 characters or more!")
    else:
        print(f"\t{i} is only {len(i)} long!")