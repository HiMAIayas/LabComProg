n = int(input("Enter an integer number: "))
print("O "*n)
for i in range(n-2):
    print("O " + "  "*i + "X "*(n-2-i) + "O")
print("O "*n)