sen = input("Input a sentence: ").split()
dupList = []
wordList=[]
for i in sen:
    if i in wordList and i not in dupList:dupList.append(i.lower())
    else:wordList.append(i)

print("Output:")
if len(dupList)==0:print("none")
else:
    for i in dupList:
        print(i)
    