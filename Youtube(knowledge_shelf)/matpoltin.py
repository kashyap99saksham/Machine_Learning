import numpy as np
# MATPOTLIN : USING FOR DATA PLOTING
import matplotlib.pyplot as plt
a = [2,4,6,9,3]
b = [2,2,4,4,5]
plt.plot(a,b)
plt.grid()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('First Graph')
plt.show()      #GIVES GRAPH

# WORK OF MATPLOTLIB WITH NUMPY
a = np.arange(1,8,2)
b= np.arange(2,9,2)
plt.plot(a,b,'g')   #green color :-)
plt.grid()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()


