import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y= [10,24,36,40,5]  #SHOULD BE SAME NO. OF INPUTS IN BOTH
t_l = ['india','pak','us','china','russia']
plt.bar(x,y,tick_label = t_l,width=0.8,color=['red','green'])
plt.show()