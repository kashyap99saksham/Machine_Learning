import matplotlib.pyplot as plt
x = [ 120,60,76,50,87,90,53,67,150]
y = [ 110,54,86,30,97,70,93,57,170]
plt.scatter(x,y,label='stars',marker = "*",s=120)       #s is size of star , marker is used to tell print in *
plt.legend()        #legend is used to tell about graph , for more info see fig. top
plt.show()