import matplotlib.pyplot as plt


xvalues = list(range(1,1001))
yvalues = [x**2 for x in xvalues]

plt.scatter(xvalues,yvalues,c=yvalues,edgecolor='none',s=40)
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,1100,0,1100000])
plt.show()
# plt.savefig('squares_plot.png',bbox_inches='tight')