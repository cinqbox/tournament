def upper_winrate(upper_rate, lower_rate):
    """上位者が勝つ確率"""
    return 1 - 1 / (10 ** ((upper_rate - lower_rate) / 400) + 1)


def lower_winrate(upper_rate, lower_rate):
    return 1 / (10 ** ((upper_rate - lower_rate) / 400) + 1)
