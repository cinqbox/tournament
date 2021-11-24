import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

xl = []
yl = []

for x in range(-1000, 1000):
    y = 100 - 100 / (10 ** (x / 400) + 1)
    xl.append(x)
    yl.append(y)

plt.title("EloRating WinRate")

plt.plot(xl, yl)
plt.show()
