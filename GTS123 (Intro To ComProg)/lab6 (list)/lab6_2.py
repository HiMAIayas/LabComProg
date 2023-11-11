numList = input("Enter a comma-separated list: ").split(",")
for i in numList:
    for j in numList:
        if j>i:
            for k in numList:
                if k>j:
                    print(i,j,k)