import math as m

paint=float(input("Input the covered area for one paint bottle (cm square): "))
n=int(input("Input the number of the spheres: "))
rad=float(input("Input the radius of each sphere (cm): "))

idk=m.ceil(4*m.pi*(rad**2)*n/paint)
print(f"The paint bottles are needed to paint the surface of spheres is {idk}.")