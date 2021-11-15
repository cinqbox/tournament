from .win_rate import upper_winrate
import numpy as np



def game_judge(upper_rate, lower_rate):
    """勝ち負け判定関数"""
    up_winrate = upper_winrate(upper_rate, lower_rate)
    n = up_winrate * 10 ** 4
    r = np.random.randint(0, 9999)
    # print("n:{}, r:{}".format(n, r))
    if r < n:  # 上位者勝ち
        return True
    else:  # 下位者勝ち
        return False
