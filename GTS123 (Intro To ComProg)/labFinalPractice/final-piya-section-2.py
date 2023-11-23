def printStock(stock):
    for keys in stock:
        print(f'{keys}: {stock[keys][0]}')
    
pricep={
    'Mango':13,
    'Durian':50,
    'Pineapple':40,
    'Banana':5,
    'Watermelon':30
}

stock={
    'Mango':50,
    'Durian':50,
    'Pineapple':50,
    'Banana':50,
    'Watermelon':50
}
print(stock)

order=input("Input Fruits Item: ").split(',')
price=0


for fruit in order:
    fruit_name, fruit_amount = fruit.split()
    fruit_amount = int(fruit_amount)
    
    if fruit_name in stock:
        if stock[fruit_name]>=fruit_amount:
            stock[fruit_name]-=fruit_amount
            price+=pricep[fruit_name]*fruit_amount
        else:
            print(f"Sorry, {fruit_name} is not available")
    else:
        print(f"Sorry, {fruit_name} is not available")
        
print(f"The overall amount due for your order = {price}")
print(stock)
            