n = int(input("Enter an integer number: "))
print("O "*n)
for i in range(n-2):
    print("O " + "  "*(n-2) +"O")
print("O "*n)