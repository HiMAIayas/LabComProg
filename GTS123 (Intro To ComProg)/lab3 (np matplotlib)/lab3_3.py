import math as m

h=float(input("Enter the pentagon height: "))

a=2*h/m.sqrt(5+2*m.sqrt(5))
A=(a**2)*m.sqrt(25+10*m.sqrt(5))/4

print(f"The length for one side of the pentagon is {a:.4f}.")
print(f"The pentagon area and perimeter are {A:.4f} and {5*a:.4f}.")