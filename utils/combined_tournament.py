from .game_judge import game_judge
import random
import pprint
import copy
import numpy as np


def combined_tournament(rate_dic):
    """スイスドロー + ダブルエリミネーション"""
    # スイスドロー（予選）部分
    win_sorted = copy.deepcopy(rate_dic)
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
                    player1['won_users'].append(player2['rate_rank'])
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

    win_sorted = sorted(win_sorted, key=lambda x: x['rate_rank'])

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
        if flg_win == data['win'] and flg_sb == data['sb'] and flg_solkov == data['solkov'] and flg_medium == data['medium']:  # 同率で並んでいるとき
            tmp += 1
            data['win_rank'] = rank
            flg_win, flg_sb, flg_solkov, flg_medium = data['win'], data['sb'], data['solkov'], data['medium']
        else: # 順位が異なる時
            rank += tmp
            data['win_rank'] = rank
            tmp = 1
            flg_win, flg_sb, flg_solkov, flg_medium = data['win'], data['sb'], data['solkov'], data['medium']

    swissed_data = sorted(win_sorted, key=lambda x: x['win_rank'], reverse=True)


    # ダブルエリミ部分（決勝T）
    losed_user = swissed_data[:-16]
    upper_bracket = swissed_data[-16:]
    random.shuffle(upper_bracket)
    lower_bracket = []
    eliminate = []
    winner = 4  # 勝ち残り数, log2(16)
    rank_list = [16, 12, 8, 6, 4, 3]  # 敗退プレイヤーの順位
    r = 0

    for i, player in enumerate(upper_bracket):
        player['battle_order'] = i + 1
        player['losed_user'] = []

    for i in range(winner):
        # ランダムに2者を選択させて対戦させる
        # winner_bracket
        for j in range(0, len(upper_bracket), 2):
            player1, player2 = upper_bracket[j:j + 2]
            if player1['rate'] > player2['rate']:
                flg = game_judge(player1['rate'], player2['rate'])
                if flg:
                    player1['win'] += 1
                    player2['lose'] += 1
                    player1['matches'] += 1
                    player2['matches'] += 1
                    player2['losed_user'].append(player1['rate_rank'])
                else:
                    player2['win'] += 1
                    player1['lose'] += 1
                    player1['matches'] += 1
                    player2['matches'] += 1
                    player1['losed_user'].append(player2['rate_rank'])
            else:
                flg = game_judge(player2['rate'], player1['rate'])
                if flg:
                    player2['win'] += 1
                    player1['lose'] += 1
                    player1['matches'] += 1
                    player2['matches'] += 1
                    player1['losed_user'].append(player2['rate_rank'])
                else:
                    player1['win'] += 1
                    player2['lose'] += 1
                    player1['matches'] += 1
                    player2['matches'] += 1
                    player2['losed_user'].append(player1['rate_rank'])

        upper_bracket = sorted(upper_bracket, key=lambda x: (x['win'], x['battle_order']), reverse=True)
        lower_bracket += upper_bracket[len(upper_bracket) // 2:]
        upper_bracket = upper_bracket[:len(upper_bracket) // 2]

        # pprint.pprint(upper_bracket)
        print(len(upper_bracket), len(lower_bracket), len(eliminate))
        print('======================[Upper_Left{}]========================'.format(len(upper_bracket)))

        # lower_bracket
        lower_bracket = sorted(lower_bracket, key=lambda x: (-x['win'], x['lose'], x['battle_order']))
        while len(upper_bracket) // 2 < len(lower_bracket) and len(lower_bracket) > 1:
            r += 1
            for k in range(0, len(lower_bracket), 2):
                player1, player2 = lower_bracket[k:k + 2]
                if player1['rate'] > player2['rate']:
                    flg = game_judge(player1['rate'], player2['rate'])
                    if flg:
                        player1['win'] += 1
                        player2['lose'] += 1
                        player1['matches'] += 1
                        player2['matches'] += 1
                        player2['win_rank'] = rank_list[r - 1]
                        player2['losed_user'].append(player1['rate_rank'])
                    else:
                        player2['win'] += 1
                        player1['lose'] += 1
                        player1['matches'] += 1
                        player2['matches'] += 1
                        player1['win_rank'] = rank_list[r - 1]
                        player1['losed_user'].append(player2['rate_rank'])
                else:
                    flg = game_judge(player2['rate'], player1['rate'])
                    if flg:
                        player2['win'] += 1
                        player1['lose'] += 1
                        player1['matches'] += 1
                        player2['matches'] += 1
                        player1['win_rank'] = rank_list[r - 1]
                        player1['losed_user'].append(player2['rate_rank'])
                    else:
                        player1['win'] += 1
                        player2['lose'] += 1
                        player1['matches'] += 1
                        player2['matches'] += 1
                        player2['win_rank'] = rank_list[r - 1]
                        player2['losed_user'].append(player1['rate_rank'])
                # print("=====対戦組み合わせ========")
                # print(player1['rate_rank'], player2['rate_rank'])
                # print("===========================")

            # 勝ち数で並び替え
            lower_bracket = sorted(lower_bracket, key=lambda x: (x['lose'], -x['win'], x['battle_order']))
            eliminate += lower_bracket[len(lower_bracket) // 2:]
            lower_bracket = lower_bracket[:len(lower_bracket) // 2]

            # pprint.pprint(lower_bracket)
            # print('=================================================================')
            # pprint.pprint(eliminate[-len(lower_bracket):])
            print(r, rank_list[r-1])
            print(len(upper_bracket), len(lower_bracket), len(eliminate))
            print('======================[Lower_Left{}]========================'.format(len(lower_bracket)))

    # 決勝戦
    player1, player2 = lower_bracket[0], upper_bracket[0]
    if player1['rate'] > player2['rate']:
        flg = game_judge(player1['rate'], player2['rate'])
        if flg:
            player1['win'] += 1
            player2['lose'] += 1
            player1['matches'] += 1
            player2['matches'] += 1
            player1['win_rank'] = 1
            player2['win_rank'] = 2
            player2['losed_user'].append(player1['rate_rank'])
        else:
            player2['win'] += 1
            player1['lose'] += 1
            player1['matches'] += 1
            player2['matches'] += 1
            player2['win_rank'] = 1
            player1['win_rank'] = 2
            player1['losed_user'].append(player2['rate_rank'])

    else:
        flg = game_judge(player2['rate'], player1['rate'])
        if flg:
            player2['win'] += 1
            player1['lose'] += 1
            player1['matches'] += 1
            player2['matches'] += 1
            player2['win_rank'] = 1
            player1['win_rank'] = 2
            player1['losed_user'].append(player2['rate_rank'])

        else:
            player1['win'] += 1
            player2['lose'] += 1
            player1['matches'] += 1
            player2['matches'] += 1
            player1['win_rank'] = 1
            player2['win_rank'] = 2
            player2['losed_user'].append(player1['rate_rank'])

    result_list = upper_bracket + lower_bracket + eliminate
    result_list = sorted(result_list, key=lambda x: x['win_rank'], reverse=True)
    return_data = result_list + losed_user
    return_data = sorted(return_data, key=lambda x: x['win_rank'], reverse=True)
    # return_data = sorted(return_data, key=lambda x: x['rate'])

    # pprint.pprint(return_data)

    for data in result_list:
        print(data['win_rank'])

    return return_data
