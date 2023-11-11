import math as m

cube_side=float(input("Enter the width of the cube: "))
con_w=float(input("Enter the width of the container: "))
con_h=float(input("Enter the height of the container: "))
con_d=float(input("Enter the depth of the container: "))

ans=(con_w//cube_side) * (con_h//cube_side)*(con_d//cube_side)

print(f"The number of cubes that can fit into the container is {int(ans)}.")