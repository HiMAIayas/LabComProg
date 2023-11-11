string = input("Input: ")
for i in string:
    if i.isnumeric():
        i=int(i)
        print("**#"*(i//3) +"*"*(i%3))