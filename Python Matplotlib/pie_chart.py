import matplotlib.pyplot as plt

values = [16,18,4]
labels = ["Python ", "Ruby", "Java"]
pieexplode = [0.1,0,0]

plt.pie(values, labels = labels,explode = pieexplode, startangle =90, shadow = True)
plt.xlabel("HoriTitle")
plt.ylabel("VertTitle")
plt.title("Chart")
plt.legend(loc = 'best')
plt.show()