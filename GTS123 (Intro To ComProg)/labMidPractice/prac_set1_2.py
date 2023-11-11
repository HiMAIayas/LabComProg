N= int(input("Input: "))
if N<1 or N>15: print("Invalid input")
else:
    num=1
    for i in range(N):
        print("0\t"*i,end="")
        for j in range(N-i):
            print(num,end="\t")
            num+=1
        print()