import matplotlib.pyplot as plt

x_values = list(range(1,5000))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=(0.3,0.4,0.5), edgecolor='none', s=40)

plt.axis([0, 5001, 0, 125000000000])

plt.show()
