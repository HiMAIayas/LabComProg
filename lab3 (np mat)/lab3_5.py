import math as m

diameter=float(input("Enter the sphere diameter: "))


V=m.pi*(diameter**3)/6
area=m.pi*(diameter**2)

print(f"The length of the sphere radius is {diameter/2:.4f}.")
print(f"The sphere volume and the surface area are {V:.4f} and {area:.4f}.")