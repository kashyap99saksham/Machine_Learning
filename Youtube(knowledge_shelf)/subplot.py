# SUBPLOT
import numpy as np
import matplotlib.pyplot as plt
x1=np.arange(1,10)
x2=np.arange(1,10)
y1=np.arange(1,10)
y2=np.arange(1,10)

plt.subplot(2,1,1)
plt.plot(x1,y1,'o-')
plt.show()


plt.subplot(2,1,2)
plt.plot(x2,y2,'r')
plt.show()

