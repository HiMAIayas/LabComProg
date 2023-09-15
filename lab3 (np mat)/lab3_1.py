import math as m
import numpy as np
import matplotlib.pyplot as plt


x=np.arange(-3*m.pi,3*m.pi,0.01)
y1=np.sin(x)
y2=np.sin(x+0.5)
y3=np.sin(x+1)
y4=np.sin(x+1.5)

plt.plot(x,y1,color="blue",linestyle="dotted")
plt.plot(x,y2,color="green",linestyle="dashed")
plt.plot(x,y3,color="orange",linestyle="dashdot")
plt.plot(x,y4,color="pink",linestyle="solid")
plt.show()


