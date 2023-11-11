import math as m
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(10,0,-0.1)
y=(1+x)/np.sqrt(x)

plt.plot(x,y,color="blue")
plt.show()
