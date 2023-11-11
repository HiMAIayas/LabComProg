wordList = []
while True:
    s = input("Input: Enter a word: ")
    if s == "exit":break
    if s[-1]=="y": s = s[:-1] +"ily"
    wordList.append(s)
    
print("Output: ",wordList)