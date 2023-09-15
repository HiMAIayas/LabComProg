even,odd=0,0
for i in range(5):
    num=int(input("Enter a number: "))
    if num%2==0:even+=1
    else:odd+=1
print(f"There is/are {even} even numbers")
print(f"There is/are {odd} odd numbers")