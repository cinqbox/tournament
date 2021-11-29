from utils import *
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


for model in [round_robin, single_elimination, double_elimination, swiss_draw]:
    # 順位変動分散比較まとめグラフ作成
    # rate_list = rating(6400, 0)  # 1000~1945 15刻み
    rate_list = normalize_rating(1500, 200)
    trial_num = 2000
    true_count = 0
    x_rating = []
    win_rank_var_score_list = []

    for i in range(trial_num):
        if model == double_elimination:
            result = model(rate_list, 64)
        else:
            result = model(rate_list)
        for j, data in enumerate(result):
            rate_list[63 - j]['win_rank_list'].append(data['win_rank'])

    for data in rate_list:
        x_rating.append(data['rate'])
        win_rank_var_score_list.append(np.var(data['win_rank_list']))

    left = x_rating[::-1]
    # print(min(win_rank_var_score_list))
    height = win_rank_var_score_list[::-1]
    plt.title('variance comparison between models')
    plt.xlabel('Rating')
    plt.ylabel('Variance')
    plt.plot(left, height)
    plt.legend(labels=['RoundRobin', 'SingleElimination', 'DoubleElimination', 'SwissDraw'])
plt.show()