while True:
    amount = float(input("Enter initial amount: "))
    if amount>0:break
    else:print("please enter .......")

while True:
    rate = float(input("Enter annual rate: "))
    if rate>0:break
    else:print("please enter .......")
    
while True:
    year = int(input("Enter number of years: "))
    if year>0:break
    else:print("please enter .......")
    
print('-------------')
for i in range(year):
    amount*=1+rate/100
    print(f"Year {i}: Total savings = {amount:.2f}")
    
print(f'\nAfter {year} years, the total amount saved will be: {amount:.2f}')
    
    

    