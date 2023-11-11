import math
def myCylinder(r,h):
    v=math.pi*(r**2)*h
    a=2*math.pi*r*(r+h)
    return v,a

r=float(input("Enter the radius r of the cylinder: "))
h=float(input("Enter the height h of the cylinder: "))
v,a = myCylinder(r,h)
print(f"The volume us {v:.2f} and the surface area is {a:.2f}")