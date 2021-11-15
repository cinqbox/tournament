from utils import *
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 結果確認用
# rate_list = rating(6400, 0)
rate_list = normalize_rating(1000, 100)
trial_num = 10**3  # 10**4
true_count = 0
x_rating = []
y_rank_difference = []
in_order_rank_count_list = []

for i in range(trial_num):
    double_el = double_elimination(rate_list, 64)
    rank = 1000  # 前のデータの順位を保存
    in_order_rank_count = -1  # 一番最初で0にするため
    for j, data in enumerate(double_el):
        if data['win_rank'] <= rank:
            in_order_rank_count += 1
        rate_list[63 - j]['win_rank_list'].append(data['win_rank'])
        rank = data['win_rank']
    in_order_rank_count_list.append(in_order_rank_count)

for data in rate_list:
    x_rating.append(data['rate'])
    data['avg_rank'] = sum(data['win_rank_list']) / trial_num
    y_rank_difference.append((data['rate_rank'] - data['avg_rank']) ** 2)  # R^2誤差
    print(
        f"レーティング:{data['rate']} 平均順位{round(data['avg_rank'], 2)}位, 予想順位{data['rate_rank']}位, 順位の分散{np.var(data['win_rank_list'])}")

for i in range(len(rate_list) - 1):
    if rate_list[i]['avg_rank'] < rate_list[i + 1]['avg_rank']:
        true_count += 1
print("順番通りの割合:{}".format(true_count / 63))
# print(sum(in_order_rank_count_list) / trial_num)

left = x_rating[::-1]
height = y_rank_difference[::-1]

plt.plot(left, height)
plt.show()
