cus = int(input("Input number of customers: "))
disCode = input("Input discount code: ")
price = min(599,399+100*((cus-1)//3))
if disCode=="CASH":dis=0.95
elif disCode=="BIRTHDAY":dis=0.9
elif disCode=="COVID":dis=0.7
else:dis=1

total=cus*price
print(f"{cus} person x {price:.2f} baht = {total:.2f}")
print(f"On-top discount {int((1-dis)*100)}%")
print(f"Total price is {total*dis:.2f}")