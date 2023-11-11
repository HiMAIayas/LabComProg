while True:
    inp = input("Enter an integer number ('X' to exit): ")
    if inp=="X":break
    try: inp=int(inp)
    except:continue
    
    for i in range(inp):
        for j in range(inp):
            if j==i or j==inp-i-1:print("X",end=" ")
            else:print(".",end=" ")
        print()