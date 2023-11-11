numStr = input("Input: ").split()
numList = [int(i) for i in numStr if i.isnumeric()]
dic = dict()
for i in numList:
    if i in dic:dic[i]+=1
    else:dic[i]=1


output="good sentence"
for key in dic:
    if key!=dic[key]:
        output="bad sentence"

print("Output:",output)