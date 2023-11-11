print("=======Welcome to Hi!! Car Wash=======")
ser=input("Choose your services: W=Wash C=Wash+Vacuum: ").lower()

if ser=="w" or ser=="c":
    size=input('Enter your car size: "S","M","L" : ').lower()
    if ser=="w":
        if size=="s":print("Price = 100 baht")
        elif size=="m":print("Price = 120 baht")
        elif size=="l":print("Price = 140 baht")
        else:print("You enter the wrong car size")
    else:
        if size=="s":print("Price = 120 baht")
        elif size=="m":print("Price = 140 baht")
        elif size=="l":print("Price = 160 baht")
        else:print("You enter the wrong car size")
    
else:print("Please choose your service")
