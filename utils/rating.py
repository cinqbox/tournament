import numpy as np


def rating(upper_rate, lower_rate):
    """等間隔レーティング"""
    rate_list = []
    for i, rate in enumerate(range(lower_rate, upper_rate, 100)[::-1]):
        data = {
            'rate_rank': i + 1,
            'rate': rate * 0.15 + 1000,
            'win': 0,
            'lose': 0,
            'matches': 0,
            'win_rank': 0,
            'avg_rank': 0,
            'win_rank_list': [],
        }
        rate_list.append(data)

    return rate_list


def normalize_rating(mean, std):
    rate_list = []
    np.random.seed(64)  # seedは固定
    x = np.random.normal(mean, std, 64)
    x.sort()
    for i, rate in enumerate(x[::-1]):
        data = {
            'rate_rank': i + 1,
            'rate': rate,
            'win': 0,
            'lose': 0,
            'matches': 0,
            'win_rank': 0,
            'avg_rank': 0,
            'win_rank_list': [],
        }
        rate_list.append(data)
    return rate_list
