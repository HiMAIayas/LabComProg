money=float(input("Enter the money you have: "))
price=float(input("Enter the price of item: "))
tax=price*0.08
price+=tax
print("Tax =",tax)
print("Total price =",price)
if money>=price:print("Yes, You have enough money to buy.")
else:print(f"No, youhave shortfall of {price-money}, you cannot buy.")