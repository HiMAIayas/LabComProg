s = input("Enter a string: ")
re_s = ""
for i in s:
    if i.lower()==i:re_s+=i.upper()
    else: re_s+=i.lower()
print(f"reverse string output: {re_s}")