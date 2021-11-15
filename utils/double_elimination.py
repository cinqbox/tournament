from .game_judge import game_judge
import numpy as np
import random
import copy


def double_elimination(rate_dic, player_num):
    upper_bracket = copy.deepcopy(rate_dic)
    lower_bracket = []
    eliminate = []
    winner = int(np.log2(player_num))  # 勝ち残りの数 # log2(16)
    random.shuffle(upper_bracket)  # 組み合わせ抽選
    rank_list = [64, 48, 32, 24, 16, 12, 8, 6, 4, 3]  # 敗退プレイヤーの順位
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
        # print(len(upper_bracket), len(lower_bracket), len(eliminate))
        # print('======================[Upper_Left{}]========================'.format(len(upper_bracket)))

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
            # print(len(upper_bracket), len(lower_bracket), len(eliminate))
            # print('======================[Lower_Left{}]========================'.format(len(lower_bracket)))

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
    return_data = sorted(result_list, key=lambda x: x['rate'])
    return return_data
