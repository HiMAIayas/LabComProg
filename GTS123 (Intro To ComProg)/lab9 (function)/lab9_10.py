
import math
def SquareArea(x):
    return x**2
def CircleArea(r):
    return math.pi*r**2


mode = input("Do you want to find the area of a square (s) or a circle (c)?: ")
if mode=="s" or mode=="c":
    len=int(input("Enter the lenght: "))
    print()
    if mode=="s":print(f"The area of the square is {SquareArea(len):.2f}")
    else:print(f"The area of the circle is {CircleArea(len):.2f}")

else:print("\nWrong Input")