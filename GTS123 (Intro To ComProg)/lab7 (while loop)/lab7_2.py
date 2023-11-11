wordList = []
while True:
    s = input("Input: Enter a word: ")
    if s == "exit":break
    s=s.capitalize()
    if s not in wordList: wordList.append(s)
    
print("Output: ",wordList)