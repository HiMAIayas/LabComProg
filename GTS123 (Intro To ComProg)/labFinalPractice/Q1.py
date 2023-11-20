money = int(input("Enter the initial balance: "))

while True:
    try:
        act,num = input("Transaction type and amount (\"done 0\" to exit): ").split()
    except:
        print("Invalid input, please try again.")
        continue
    
    if act=="done":
        break
    
    if act in ["W","D"] and num.isnumeric() and int(num)>=0:
        num=int(num)
        if act=="D":
            money+=num
            print(f"> Deposit = {num} THB, current balance = {money} THB.")
        else: #withdraw
            if money<num: print("> Invalid transaction")
            else:
                money-=num
                print(f"> Withdrawal = {num} THB, current balance = {money} THB.")
    else:
        print("> Invalid transaction")
        
print(f"Current balance = {money} THB")