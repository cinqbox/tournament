from .game_judge import game_judge
import random
import pprint
import copy


def single_elimination(rate_dic):
    """シングルエリミネーション"""
    win_sorted = copy.deepcopy(rate_dic)
    result_list = []
    winner = [64, 32, 16, 8, 4, 2]  # 勝ち残りの数
    random.shuffle(win_sorted)  # 組み合わせ抽選

    for i, player in enumerate(win_sorted):
        player['battle_order'] = i + 1
        player['losed_user'] = []

    for i in winner:
        # 勝ち数で並び替え
        win_sorted = sorted(win_sorted, key=lambda x: (x['win'], x['battle_order']), reverse=True)
        result_list += win_sorted[i:]
        win_sorted = win_sorted[:i]
        # pprint.pprint(win_sorted)
        # print('======================[Round{} Finish]========================'.format(i))

        # print(result_list, win_sorted)

        # ランダムに2者を選択させて対戦させる
        for j in range(0, i, 2):
            player1, player2 = win_sorted[j:j + 2]
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

    result_list += win_sorted
    result_list = sorted(result_list, key=lambda x: x['win'], reverse=True)
    for result in result_list:
        if result['win'] == 0:
            result['win_rank'] = 64
        elif result['win'] == 1:
            result['win_rank'] = 32
        elif result['win'] == 2:
            result['win_rank'] = 16
        elif result['win'] == 3:
            result['win_rank'] = 8
        elif result['win'] == 4:
            result['win_rank'] = 4
        elif result['win'] == 5:
            result['win_rank'] = 2
        else:
            result['win_rank'] = 1

    return_data = sorted(result_list, key=lambda x: x['rate'])
    return return_data
