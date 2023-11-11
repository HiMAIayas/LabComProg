speed = input("Speed = ")
if not speed.isnumeric():print("Invalid input")
else:
    speed=int(speed)
    if speed<=0:print("Invalid input")
    else:
        dis = input("Distance = ")
        if not dis.isnumeric():print("Invalid input")
        else:
            dis=int(dis)
            if dis<=0:print("Invalid input")
            else: 
                form = input("Format (D/M) = ")
                time=dis/speed
                if form=="D":
                    print(f"At {speed} mph, it will take")
                    print(f"{time:.2f} hours to travel {dis} miles.")
                elif form=="M":
                    print(f"At {speed} mph, it will take")
                    print(f"{int(time)} hours and {round((time%1)*60)} minutes to travel {dis} miles.")
                else:print("Invalid input")
                