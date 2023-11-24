#This program is designed to handle the negative integer case, 
#and the wrong amount of input numbers case :D
import numpy as np

coefList = list()
mat2 = np.zeros((3,1))

valid=True

for i in range(3):
    tempL = input(f"Please provide the input values for a{i*4}, a{i*4+1}, a{i*4+2}, and a{i*4+3}: ").split()
    if len(tempL)!=4: valid=False
    for num in tempL:
        try:
            if int(num)!=float(num): #it is not an integer
                raise Exception
        except:
            valid=False
    
    if valid: 
        coefList.append([int(j) for j in tempL[0:3]])
        mat2[i]=tempL[3]
        
if not valid:print("Please enter only integer values.")
else:
    mat1 = np.array(coefList)
    if np.linalg.det(mat1)==0:
        print("The solution does not exist!")
    else:
        ans = np.matmul(np.linalg.inv(mat1),mat2)
        print(f'The minimum value in the solution vector = {min(ans)[0]:.2f}')
        print(f'The maximum value in the solution vector = {max(ans)[0]:.2f}')
        print(f'The average of the values in the solution vector = {sum(ans)[0]/len(ans):.2f}')
        