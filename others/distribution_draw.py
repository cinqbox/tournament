import matplotlib
from utils import *
import numpy as np

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# rate_list = rating(6400, 0)  # 1000~1945 15刻み
# rate_list = normalize_rating(1500, 200)
rate_list = two_mountain_rating(1250, 1700, 100)
rate_list = list(map(lambda x: x['rate'], rate_list))

plt.hist(rate_list, bins=16, ec='black')
plt.title("Rating histogram")
plt.xlabel("Rating")
plt.ylabel("Frequency")

plt.show()