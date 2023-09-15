money=int(input("Amount of money you would like to withdraw: "))
print("we may give you:")
if money>=500:
    print(f"{money//500} bills(s) of 500 baht.")
    money=money%500
if money>=100:
    print(f"{money//100} bills(s) of 500 baht.")
    money=money%100
if money>=50:
    print(f"{money//50} bills(s) of 500 baht.")
    money=money%50
if money>=2:
    print(f"{money//2} coins(s) of 500 baht.")
    money=money%2
if money>=1:
    print(f"{money} coins(s) of 500 baht.")
