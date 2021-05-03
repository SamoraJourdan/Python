import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [2,4,6,8,10,2,4,6]

plt.plot(x, y, 'b-.', linewidth = 4.0)
plt.axis([0,10,0,10])
plt.xlabel("Horizontal Title")
plt.ylabel("Vertical Title")
plt.title("Graph")
plt.show()