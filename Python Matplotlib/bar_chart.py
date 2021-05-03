import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]

colors = ['green', 'red', 'blue', 'orange', 'yellow' ]

plt.barh(x1,y1, edgecolor = 'black', color = colors, linewidth = 4)
plt.xlabel("Horizontal Title")
plt.ylabel("Vertical Title")
plt.title("Graph")
plt.show()