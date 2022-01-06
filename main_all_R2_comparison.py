from utils import *
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


for model in [round_robin, single_elimination, double_elimination, swiss_draw]:
    # R順位と実順位の差のR^2誤差まとめグラフ作成
    # rate_list = rating(6400, 0)  # 1000~1945 15刻みに誤差を加える
    rate_list = normalize_rating(1500, 200)
    trial_num = 200
    true_count = 0
    x_rating = []
    y_rank_difference = []

    for i in range(trial_num):
        if model == double_elimination:
            result = model(rate_list, 64)
        else:
            result = model(rate_list)
        for j, data in enumerate(result):
            rate_list[63 - j]['win_rank_list'].append(data['win_rank'])

    for data in rate_list:
        x_rating.append(data['rate'])
        data['avg_rank'] = sum(data['win_rank_list']) / trial_num
        y_rank_difference.append((data['rate_rank'] - data['avg_rank']) ** 2)  # R^2誤差

    left = x_rating[::-1]
    height = y_rank_difference[::-1]
    plt.title('R^2 comparison between models')
    plt.xlabel('Rating')
    plt.ylabel('R^2')
    plt.plot(left, height)
    plt.legend(labels=['RoundRobin', 'SingleElimination', 'DoubleElimination', 'SwissDraw'])
plt.show()