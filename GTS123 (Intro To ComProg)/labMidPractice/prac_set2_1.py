import math
shape = input("Input a shape T/S/C: ")
d = float(input("Input a length: "))
if d<0:print("Length must be more than or equal to zero.")
else:
    if shape=="T":print(f"The surface area of triangle is {d**2/4:.2f}")
    elif shape=="S":print(f"The surface area of square is {d**2/2:.2f}")
    elif shape=="C":print(f"The surface area of circle is {math.pi*d**2/4:.2f}")
    else:print("Type must be onlt T/S/C")