import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection= '3d')

N = 10
x1 = np.random.rand(N)
y1 = np.random.rand(N) 
z1 = np.random.rand(N)
x2 = np.random.rand(N)
y2 = np.random.rand(N) 
z2 = np.random.rand(N)



ax.scatter(x1, y1, z1, s=20, color = 'red' , marker ='^')
ax.scatter(x2, y2, z2, s=20, color = 'green' , marker ='o')
plt.show()
