import numpy as np

path="sales.tsv"
data = np.loadtxt(path)


value = np.sum(data[:,1:],axis=1)
index_arr = np.argsort(value)[::-1]

for iterator in index_arr:
    print(f"{data[iterator][0]:.0f}\t{value[iterator]}")
