x=float(input("Enter x = "))
y=float(input("Enter y = "))


alpha=(-2*(x-1)-(y-2))/4
beta=(2-y)/4
gamma=1-alpha-beta

if alpha>0 and beta>0 and gamma>0:print("Point (x,y) inside polygon")
else:print("Point (x,y) outside polygon")