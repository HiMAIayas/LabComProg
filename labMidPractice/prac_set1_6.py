dna = input("DNA: ")
base = input("Base: ")
if dna.isalpha() and base.isalpha():
    count_=0
    for i in dna:
        if base==i:count_+=1
    print(f"There are {count_} times that the base C occur in this DNA.")
else:print("Invalid input")