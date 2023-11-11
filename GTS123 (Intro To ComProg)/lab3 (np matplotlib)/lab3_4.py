import math as m

x1=float(input("Enter coordinate X for P1: "))
y1=float(input("Enter coordinate Y for P1: "))
x2=float(input("Enter coordinate X for P2: "))
y2=float(input("Enter coordinate Y for P2: "))

diameter=m.sqrt((x1-x2)**2+(y1-y2)**2)
area=m.pi*(diameter**2)/4
circum=m.pi*diameter

print(f"The length of the circle diameter is {diameter:.4f}.")
print(f"The circle area and circumference are {area:.4f} and {circum:.4f}.")
