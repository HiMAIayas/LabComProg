char = input("Enter a character: ")
size = int(input("Enter a size: "))
opt = input("Enter an option: ")
if (char not in "#$@*^") or (opt not in ["1","2"]):print("Invalid input")
else:
    for i in range(size):
        if opt=="1": print(". "*i + char + " ."*(size-i-1))
        else: print(". "*(size-i-1) + char + " ."*i)