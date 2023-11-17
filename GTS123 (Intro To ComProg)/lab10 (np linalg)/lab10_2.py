import numpy as np

coef = np.zeros((3,3))
rhs = np.zeros((3,1))
for i in range(3):
    for j in range(3):
        coef[i][j] = int(input(f"Input C{i*4+j+1}: "))
    rhs[i][0] = int(input(f"Input C{(i+1)*4}: "))
print()
try:
    ans = np.matmul(np.linalg.inv(coef),rhs)
    print("Solution:")
    print(f"x ={ans[0][0]:.2f}")
    print(f"y ={ans[1][0]:.2f}")
    print(f"z ={ans[2][0]:.2f}")
except:
    print("Unable to find a solution")
