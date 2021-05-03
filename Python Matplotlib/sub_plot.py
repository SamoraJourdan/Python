import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [2,4,6,8,10,2,4,6]

fig = plt.figure()
fig.suptitle('Plot Title')

plt.subplot(2,2,1)
plt.plot(x, y, color = 'green')
plt.subplot(2,2,2)
plt.plot(x, y, color = 'blue')
plt.subplot(2,2,3)
plt.plot(x, y, color = 'red')
plt.subplot(2,2,4)
plt.plot(x, y)
plt.show()