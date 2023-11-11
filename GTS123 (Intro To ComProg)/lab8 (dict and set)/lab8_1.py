animalDict = dict()
animalList=[i.lower() for i in input("Input: ").split()]
for s in animalList:
    if s in animalDict:
        animalDict[s]+=1
    else:
        animalDict[s]=1


print("Output:")
max_val=max(list(animalDict.values()))
print(max_val)

for key in animalDict:
    if animalDict[key]==max_val:
        print(key,"=",animalDict[key])
