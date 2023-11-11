alpha=input("Enter a single letter: ")

if alpha in ["A","B","C"]:num=2
elif alpha in ["D","E","F"]:num=3
elif alpha in ["G","H","I"]:num=4
elif alpha in ["J","K","L"]:num=5
elif alpha in ["M","N","O"]:num=6
elif alpha in ["P","R","S"]:num=7
elif alpha in ["T","U","V"]:num=8
elif alpha in ["W","X","Y"]:num=9
else:num=0

if num==0:print(f"There is no digit on the telephone that corresponds to {alpha}.")
else: print(f"The digit {num} corresponds to the letter R on the telephone.")