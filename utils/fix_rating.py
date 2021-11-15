def rating_for_single(rate_list):
    for data in rate_list:
        if data['rate_rank'] > 32:
            data['rate_rank'] = 64
        elif data['rate_rank'] > 16:
            data['rate_rank'] = 32
        elif data['rate_rank'] > 8:
            data['rate_rank'] = 16
        elif data['rate_rank'] > 4:
            data['rate_rank'] = 8
        elif data['rate_rank'] > 2:
            data['rate_rank'] = 4
        elif data['rate_rank'] > 1:
            data['rate_rank'] = 2
        else:
            data['rate_rank'] = 1
    return rate_list


def rating_for_double(rate_list):
    for data in rate_list:
        if data['rate_rank'] > 48:
            data['rate_rank'] = 64
        elif data['rate_rank'] > 32:
            data['rate_rank'] = 48
        elif data['rate_rank'] > 24:
            data['rate_rank'] = 32
        elif data['rate_rank'] > 16:
            data['rate_rank'] = 24
        elif data['rate_rank'] > 12:
            data['rate_rank'] = 16
        elif data['rate_rank'] > 8:
            data['rate_rank'] = 12
        elif data['rate_rank'] > 6:
            data['rate_rank'] = 8
        elif data['rate_rank'] > 4:
            data['rate_rank'] = 6
        elif data['rate_rank'] > 3:
            data['rate_rank'] = 4
        elif data['rate_rank'] > 2:
            data['rate_rank'] = 3
        elif data['rate_rank'] > 1:
            data['rate_rank'] = 2
        else:
            data['rate_rank'] = 1
    return rate_list