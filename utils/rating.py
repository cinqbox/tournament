import numpy as np


def random_error():
    # 誤差を生成
    return np.random.randint(-10, 10)


def rating(upper_rate, lower_rate):
    """等間隔レーティング"""
    rate_list = []
    l = range(lower_rate, upper_rate, 100)
    l = list(l)
    l.sort()
    for i, rate in enumerate(l[::-1]):
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
    l = np.random.normal(mean, std, 64)
    l = list(map(lambda x: x + random_error(), l))
    l.sort()
    for i, rate in enumerate(l[::-1]):
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


def two_mountain_rating(mean1, mean2, std):
    rate_list = []
    np.random.seed(64)  # seedは固定
    l1 = np.random.normal(mean1, std, 32)
    l2 = np.random.normal(mean2, std, 32)
    l1 = list(map(lambda x: x + random_error(), l1))
    l2 = list(map(lambda x: x + random_error(), l2))
    l = l1 + l2
    l.sort()

    for i, rate in enumerate(l[::-1]):
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
