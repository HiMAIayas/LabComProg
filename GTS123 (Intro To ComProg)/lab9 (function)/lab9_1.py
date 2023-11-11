import math
def CirArea(x):
    return math.pi*x**2

def SqArea(x):
    return x**2

n=float(input("Input a positive number: "))
if n>0:
    print(f'The area of the circle is {CirArea(n):.2f}')
    print(f'The area of the square is {SqArea(n):.2f}')
else:
    print("Wrong Input")