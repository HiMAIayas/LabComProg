def sortingFunc(l):
    return l[1]

def sortDic(dic):
    return dic.items[1]
idDict = dict()
while True:
    
    inp = input("Input (DONE = exit): ")
    if inp.upper() == "DONE":break

    id,score = inp.split()
    if not (id.isnumeric() and score.isnumeric() and int(score)>=0):
        print("Invalid input")
        continue

    if id in idDict:
        print("Duplicated ID")
    else:
        idDict[id]=score

print("Output:")
iteratedList = list()
for i in idDict:
    iteratedList.append([i,idDict[i]])
iteratedList.sort(key=sortingFunc,reverse=True)
for i in iteratedList:
    print(i[0],i[1])