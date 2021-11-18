import numpy as np


def print_r1_score(score_list, trial_num):
    print(f"R1スコア平均：{sum(score_list) / trial_num}")
    print(f"R1スコア最低値：{min(score_list)}")
    print(f"R1スコア最高値：{max(score_list)}")
    print(f"R1スコア分散値：{np.var(score_list)}")


def print_r2_score(score_list, trial_num):
    print(f"R2スコア平均：{sum(score_list) / trial_num}")
    print(f"R2スコア最低値：{min(score_list)}")
    print(f"R2スコア最高値：{max(score_list)}")
    print(f"R2スコア分散値：{np.var(score_list)}")


def print_win_rank_var_score(score_list, trial_num):
    print(f"ランク分散スコア平均：{sum(score_list) / trial_num}")
    print(f"ランク分散スコア最低値：{min(score_list)}")
    print(f"ランク分散スコア最高値：{max(score_list)}")
    print(f"ランク分散スコア分散値：{np.var(score_list)}")


def print_only_score(score_list, trial_num):
    print(sum(score_list) / trial_num)
    print(min(score_list))
    print(max(score_list))
    print(np.var(score_list))
