from .game_judge import game_judge
import random
import pprint
import copy

def swiss_draw(rate_dic):
    """スイスドロー"""
    win_sorted = copy.deepcopy(rate_dic)
    result_list = []
    random.shuffle(win_sorted)  # 組み合わせ抽選

    for i, player in enumerate(win_sorted):
        player['battle_order'] = i + 1
        player['battled_users'] = []  # 対戦相手の一覧
        player['won_users'] = []  # 負かせた相手の一覧

    for i in range(6):  # 全6回戦
        win_sorted = sorted(win_sorted, key=lambda x: (x['win'], x['battle_order']), reverse=True)

        for j in range(0, 64, 2):
            player1, player2 = win_sorted[j:j + 2]
            if player1['rate'] > player2['rate']:
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
                    player2['won_users'].append(player1['rate_rank'])
            else:
                flg = game_judge(player2['rate'], player1['rate'])
                if flg:
                    player2['win'] += 1
                    player1['lose'] += 1
                    player1['matches'] += 1
                    player2['matches'] += 1
                    player1['battled_users'].append(player2['rate_rank'])
                    player2['battled_users'].append(player1['rate_rank'])
                    player2['won_users'].append(player1['rate_rank'])
                else:
                    player1['win'] += 1
                    player2['lose'] += 1
                    player1['matches'] += 1
                    player2['matches'] += 1
                    player1['battled_users'].append(player2['rate_rank'])
                    player2['battled_users'].append(player1['rate_rank'])
                    player1['won_users'].append(player2['rate_rank'])
        # print(f"================{i}回戦====================")

    win_sorted = sorted(win_sorted, key=lambda x: x['rate_rank'])
    # for i in win_sorted:
    #     print(i['rate_rank'])

    for data in win_sorted:  # ソルコフ値, sb値
        sol_cnt = 0
        sb_cnt = 0
        for battled_user in data['battled_users']:
            sol_cnt += win_sorted[battled_user - 1]['win']
        for won_user in data['won_users']:
            sb_cnt += win_sorted[won_user - 1]['win']
        data['solkov'] = sol_cnt
        data['sb'] = sb_cnt

    # 順位付け処理
    win_sorted = sorted(win_sorted, key=lambda x: (x['win'], x['sb'], x['solkov']), reverse=True)
    rank = 0
    tmp = 1
    flg_win, flg_sb, flg_solkov = -1, -1, -1
    for i, data in enumerate(win_sorted):
        if flg_win == data['win'] and flg_sb == data['sb'] and flg_solkov == data['solkov']:  # 同率で並んでいるとき
            tmp += 1
            data['win_rank'] = rank
            flg_win, flg_sb, flg_solkov = data['win'], data['sb'], data['solkov']
        else: # 順位が異なる時
            rank += tmp
            data['win_rank'] = rank
            tmp = 1
            flg_win, flg_sb, flg_solkov = data['win'], data['sb'], data['solkov']

    # pprint.pprint(win_sorted[:10])

    return_data = sorted(win_sorted, key=lambda x: x['rate_rank'], reverse=True)
    return return_data

