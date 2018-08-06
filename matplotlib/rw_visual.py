import matplotlib.pyplot as plt
from randomwalk import RandomWalk

rw = RandomWalk(20000)
rw.fill_walk()
numbers = list(range(rw.num_points))
plt.scatter(rw.xvalues,rw.yvalues,c=numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
plt.scatter(0,0,c='green',edgecolors='none',s=100)
plt.scatter(rw.xvalues[-1],rw.yvalues[-1],c="red",edgecolors='none',s=100)
plt.axes().get_xaxis().set_visible(False)
plt.show()

	