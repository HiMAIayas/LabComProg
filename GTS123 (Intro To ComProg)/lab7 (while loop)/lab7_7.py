print("===================")
print("Cashier Program")
print("===================\n")

totalPrice = 0
itemCount = 0
price=float(input("Enter item price or -1 when finished: "))

while price!=-1:
    totalPrice+=price
    itemCount+=1
    price=float(input("Enter item price or -1 when finished: "))

print(f"\nTotal purchase amount is {totalPrice}")
pay = float(input("Your payment: "))

print(f"\nYou bought {itemCount} items today.")
print(f"Your change is {pay-totalPrice} baht.")