s=input("Input: ")
valid=True
for i in s:
    if i not in ["X","O","."]:
        valid=False
        break
if len(s)!=9 or valid==False:print("Error")
else:
    print("-"*7)
    for i in range(0,9,3):
        print("|"+s[i]+"|"+s[i+1]+"|"+s[i+2]+"|")
        print("-"*7)