point = 100

while True:
    command, value = input("Command: ").split()
    value = int(value)
    if command=="done":break
    if value<0:
        print("Invalid command")
        break
    
    if command=="P":
        point+=value//50
        print(f"You earned {value//50} points")
        print(f"Your accumulated points = {point} points")
    elif command=="R":
        if point<value:
            print("Not enough points")
        else:
            point-=value
            print(f"You redeemed {value} points")
            print(f"Your accumulated points = {point} points")
    else:
        print("Invalid command")