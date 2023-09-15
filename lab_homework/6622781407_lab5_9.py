h=int(input("Height: "))
if h<1:print("Error")
else:
    for i in range(h):
        print("#"*(h-i-1) + (2*i+1)*"." + "#"*(h-i-1))