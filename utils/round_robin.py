from .game_judge import game_judge
import itertools
import copy


def round_robin(rate_dic):
    win_sorted = copy.deepcopy(rate_dic)

    for i, player in enumerate(win_sorted):
        player['battle_order'] = i + 1
        player['battled_users'] = []  # 対戦相手の一覧
        player['won_users'] = []  # 負かせた相手の一覧

    for player1, player2 in itertools.combinations(win_sorted, 2):
        # forの取り方的に必ずp1が上位者になる
        flg = game_judge(player1['rate'], player2['rate'])
        if flg:
            player1['win'] += 1
            player2['lose'] += 1
            player1['matches'] += 1
            player2['matches'] += 1
            player1['battled_users'].append(player2['rate_rank'])
            player2['battled_users'].append(player1['rate_rank'])
            player1['won_users'].append(player2['rate_rank'])
        else:
            player2['win'] += 1
            player1['lose'] += 1
            player1['matches'] += 1
            player2['matches'] += 1
            player1['battled_users'].append(player2['rate_rank'])
            player2['battled_users'].append(player1['rate_rank'])
            player1['won_users'].append(player2['rate_rank'])

    # 勝利数から順位付け
    win_sorted = sorted(win_sorted, key=lambda x: x['rate_rank'])
    # for i in win_sorted:
    #     print(i['rate_rank'])

    for data in win_sorted:  # ソルコフ値, sb値, ミディアム値
        sol_cnt = 0
        sb_cnt = []
        for battled_user in data['battled_users']:
            sol_cnt += win_sorted[battled_user - 1]['win']
        for won_user in data['won_users']:
            sb_cnt.append(win_sorted[won_user - 1]['win'])
        # print(sb_cnt)
        data['solkov'] = sol_cnt
        if not sb_cnt:
            data['sb'] = 0
            data['medium'] = 0
        else:
            data['sb'] = sum(sb_cnt)
            data['medium'] = sum(sb_cnt) - max(sb_cnt) - min(sb_cnt)

    # 順位付け処理
    win_sorted = sorted(win_sorted, key=lambda x: (x['win'], x['sb'], x['solkov'], x['medium']), reverse=True)
    rank = 0
    tmp = 1
    flg_win, flg_sb, flg_solkov, flg_medium = -1, -1, -1, -1
    for i, data in enumerate(win_sorted):
        if flg_win == data['win'] and flg_sb == data['sb'] and flg_solkov == data['solkov'] and flg_medium == data[
            'medium']:  # 同率で並んでいるとき
            tmp += 1
            data['win_rank'] = rank
            flg_win, flg_sb, flg_solkov, flg_medium = data['win'], data['sb'], data['solkov'], data['medium']
        else:  # 順位が異なる時
            rank += tmp
            data['win_rank'] = rank
            tmp = 1
            flg_win, flg_sb, flg_solkov, flg_medium = data['win'], data['sb'], data['solkov'], data['medium']
    # pprint.pprint(win_sorted[:10])

    return_data = sorted(win_sorted, key=lambda x: x['rate_rank'], reverse=True)
    return return_data
