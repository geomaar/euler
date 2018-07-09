import matplotlib.pyplot as plt

x = list(range(100))
y = [i*i*i for i in x]
plt.plot(x, y)
plt.show()