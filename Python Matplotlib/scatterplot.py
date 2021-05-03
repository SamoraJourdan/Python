import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
sns.set_style("darkgrid")

N = 250
x1 = np.random.rand(N)
y1 = np.random.rand(N) 
s1 = np.random.rand(N) *30
x2 = np.random.rand(N)
y2 = np.random.rand(N)
s2 = np.random.rand(N) *30


plt.scatter(x1, y1, s=s1)
plt.scatter(x2, y2, s=s2)
plt.xlabel("Horizontal Title")
plt.ylabel("Vertical Title")
plt.title("Graph")
plt.show()