from .game_judge import game_judge
import itertools
import copy


def round_robin(rate_dic):
    win_sorted = copy.deepcopy(rate_dic)
    for player1, player2 in itertools.combinations(win_sorted, 2):
        # forの取り方的に必ずp1が上位者になる
        flg = game_judge(player1['rate'], player2['rate'])
        if flg:
            player1['win'] += 1
            player2['lose'] += 1
            player1['matches'] += 1
            player2['matches'] += 1
        else:
            player2['win'] += 1
            player1['lose'] += 1
            player1['matches'] += 1
            player2['matches'] += 1

    # 勝利数から順位付け
    win_sorted = sorted(win_sorted, key=lambda x: x['win'], reverse=True)
    rank = 0
    tmp = 1
    flg_win = -1
    for i, data in enumerate(win_sorted):
        if data['win'] == flg_win:  # 同率で並んでいるとき
            tmp += 1
            data['win_rank'] = rank
            flg_win = data['win']
        else: # 順位が異なる時
            rank += tmp
            data['win_rank'] = rank
            tmp = 1
            flg_win = data['win']


    # 平均順位計算の為、レート順に並び替え
    return_data = sorted(win_sorted, key=lambda x: x['rate_rank'], reverse=True)
    return return_data
