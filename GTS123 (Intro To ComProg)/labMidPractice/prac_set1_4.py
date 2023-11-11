import random
width = int(input("Width = "))
height = int(input("height = "))
thick = int(input("thick = "))

for i in range(height):
    if i<thick or i>=height-thick:
        for j in range(width):
            print(random.choice(["#","$","*"]),end="")
    else:
        for j in range(thick):print(random.choice(["#","$","*"]),end="")
        print(" "*(width-2*thick),end="")
        for j in range(thick):print(random.choice(["#","$","*"]),end="")
    print()
