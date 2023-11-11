word=input("Input a word: ").strip()

print("1. ",word.upper())
print("2. ",word[0].upper()+word[1:].lower())
print("3. ",word.isnumeric())
print("4. ",word.isalpha())
print("5. ",word.upper()==word)