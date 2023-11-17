import numpy as np

P1 = np.array([float(i) for i in input("Input coordinate of P1: ").split()])
P2 = np.array([float(i) for i in input("Input coordinate of P2: ").split()])
P3 = np.array([float(i) for i in input("Input coordinate of P3: ").split()])

d=[]
d.append(np.sum((P1-P2)**2)**0.5)
d.append(np.sum((P1-P3)**2)**0.5)
d.append(np.sum((P2-P3)**2)**0.5)

print("Output:")
print(f"The longest distance = {max(d):.2f}")

