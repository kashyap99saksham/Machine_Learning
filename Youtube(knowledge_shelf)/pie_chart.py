import matplotlib.pyplot as plt
work = ['GYM','EAT','SLEEP']
slices = [3,5,10]
color = ['r','g','b']
plt.pie(slices,labels = work,colors = color,startangle=90,shadow = True,explode=(0.09,0,0),autopct = '%1.2f%%')
plt.legend()
plt.show()

# HERE LABEL IS WORK FOR Y AXIS , STARTANGLE IS TELLING ANGLE START WITH 90 DEGREE , EXPLODE IS TO HIGHLIGH SOMETHING, AUTOPCT IS CALCULATING PERCENTAGE OF EACH SLICES
