info = input("Please enter your information: ")
if info[0].isnumeric(): age, name = info.split(",")
else: name, age = info.split(",")
if name.isalpha() and age.isnumeric():
    age=int(age)
    if age<0 or age>120: print("Please enter your complete information") 
    else:
        print(f"Your name is {name}")
        print(f"Your age is {age}")
else:
    print("Please enter your complete information")