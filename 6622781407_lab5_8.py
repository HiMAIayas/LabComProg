print("Menu:\n===============")
print("A - Americano (50)")
print("E - Espresso (40)")
print("G - Green tea (60)\n")
order=input("Input: ")

sum=0
trueLen=0

print("===============")
for i in range(len(order)):
    if order[i]=="A":
        sum+=50
        print(f"{i+1}. Americano 50")
        trueLen+=1
    if order[i]=="E":
        sum+=40
        print(f"{i+1}. Espresso 40")
        trueLen+=1
    if order[i]=="G":
        sum+=60
        print(f"{i+1}. Green Tea 60")
        trueLen+=1
print("===============")
print(f"Quantity: {trueLen}")
print(f"Vat: {sum*0.07:.2f}")
print(f"Total: {sum:.2f}")
print(f"Grand Total: {sum*1.07:.2f}")
    