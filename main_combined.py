from utils import *
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 結果確認用
# rate_list = rating(6400, 0)  # 1000~1945 15刻み
rate_list = normalize_rating(1500, 200)
trial_num = 1 # 10**4
true_count = 0
x_rating = []
y_rank_difference = []
in_order_rank_count_list = []
R1_score_list = []
R2_score_list = []
win_rank_var_score_list = []

for i in range(trial_num):
    combined = combined_tournament(rate_list)
#     rank = 1000  # 前のデータの順位を保存
#     in_order_rank_count = 0  # 一番最初で0にするため
#     R1_score_sum = 0
#     R2_score_sum = 0
#     for j, data in enumerate(combined):
#         if data['rate_rank'] <= 16 and data['win_rank'] <= 16:
#             in_order_rank_count += 1
#         rate_list[63 - j]['win_rank_list'].append(data['win_rank'])
#         R1_score_sum += abs(data['rate_rank'] - data['win_rank'])
#         R2_score_sum += (data['rate_rank'] - data['win_rank']) ** 2
#         rank = data['win_rank']
#     R1_score_list.append(R1_score_sum/64)
#     R2_score_list.append(R2_score_sum/64)
#     in_order_rank_count_list.append(in_order_rank_count)
#
# for data in rate_list:
#     # x_rating.append(data['rate'])
#     data['avg_rank'] = sum(data['win_rank_list']) / trial_num
#     # y_rank_difference.append((data['rate_rank'] - data['avg_rank']) ** 2)  # R^2誤差
#     win_rank_var_score_list.append(np.var(data['win_rank_list']))
#     print(
#         f"レーティング:{data['rate']} 平均順位{round(data['avg_rank'], 2)}位, 予想順位{data['rate_rank']}位, 順位の分散{np.var(data['win_rank_list'])}")


