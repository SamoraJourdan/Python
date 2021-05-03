import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]

plt.plot(x1,y1,'ro--', label = 'student')
plt.legend(loc = 'upper left')
plt.xlabel("HoriTitle")
plt.ylabel("VertTitle")
plt.title("Chart")
plt.grid(which = 'major', linestyle = '-.', color = 'black')
plt.minorticks_on()
plt.grid(which = 'minor', linestyle = '-.', color = 'black')
plt.show()
plt.savefig("foo.png")