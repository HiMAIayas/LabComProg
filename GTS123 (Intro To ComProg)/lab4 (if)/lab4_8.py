print("Welcome to pizza online ordering")
print('Please input "y" if you wanna order, otherwise input "n"')

piz=input("Pizza?")
chi=input("Chicken?")
pas=input("Pasta?")
sal=input("Salad?")
cok=input("Coke?")
sum=0
if piz=="y":sum+=359
if chi=="y":sum+=199
if pas=="y":sum+=99
if sal=="y":sum+=99
if cok=="y":sum+=25
print("Total price is",sum)
print("Thx")