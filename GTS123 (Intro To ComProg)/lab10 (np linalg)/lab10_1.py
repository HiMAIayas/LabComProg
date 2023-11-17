import numpy as np

n=int(input("Input size of matrix: "))
arr=np.zeros((3,3))
for i in range(n):
    for j in range(n):
        arr[i][j] = int(input(f"Input element at row {i} column {j}: "))

print("Output:\nMatrix =")
print(arr)
print(f"Determinant = {np.linalg.det(arr)}")
print("Inverse matrix =")
try:
    inverse = np.linalg.inv(arr)
    print(inverse)
except:
    print("Error, this matrix is not inversible")