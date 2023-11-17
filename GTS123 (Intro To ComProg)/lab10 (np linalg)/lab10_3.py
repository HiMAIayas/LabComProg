import numpy as np

path="grade.tsv"
data = np.loadtxt(path)

grade=data[:,1:]

summ=np.sum(grade*np.array([3,2,1,3,3,3]),axis=1)/15
print("Student ID\tGPA")
for i in range(len(summ)):
    print(f"{data[i][0]:.0f}\t{summ[i]:.2f}")