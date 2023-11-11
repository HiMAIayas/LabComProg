import math as m

d=float(input("Enter the distance to the building: "))
theta=m.radians(float(input("Enter the elevation angle in degree: ")))
h=d*m.tan(theta)
print(f"The building height is {h:.4f}.")
