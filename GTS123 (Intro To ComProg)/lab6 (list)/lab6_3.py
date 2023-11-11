print("==================")
l=[]
for i in range(5):
    inp=input(f"Input#{i+1} :")
    l.append(float(inp))
    
option=input("Select the option: 1) Summary, 2) average, 3) min, 4) max >>> ")
if option=="1":result=sum(l)
elif option=="2":result=sum(l)/len(l)
elif option=="3":result=min(l)
elif option=="4":result=max(l)

print(f"Your result is {int(result)}")