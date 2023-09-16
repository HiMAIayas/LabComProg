h,m,s = input("Input: ").split(":")
if 0<=int(h)<=23 and 0<=int(m)<=59 and 0<=int(s)<=59:
    print(f"The number of seconds = {3600*(int(h))+60*(int(m))+int(s)}")
else:print("Invalid Time")