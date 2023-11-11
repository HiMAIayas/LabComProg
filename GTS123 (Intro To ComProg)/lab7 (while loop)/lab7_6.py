while True:
    print("===== MAIN MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit\n")
    
    option = int(input("Select an operation (1-3): "))
    if option==3:
        print("Bye!!!")
        break
    
    n1,n2 = [int(i) for i in input("Enter two numbers: ").split()]
    
    if option==1:
        print(f"{n1} + {n2} = {n1+n2}")
    elif option==2:
        print(f"{n1} - {n2} = {n1-n2}")
    print()