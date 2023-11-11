evenCount = 0
oddCount = 0
while True:
    n = int(input("Enter an integer (0 to exit): "))
    if n==0:break
    if n%2==0:evenCount+=1
    else:oddCount+=1

print("----------------------------------")
print(f"The number of even integers is {evenCount}")
print(f"The number of odd integers is {oddCount}")