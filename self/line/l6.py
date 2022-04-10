from bisect import bisect_left, bisect_right
from collections import defaultdict


def solution(req_id, req_info):
    trans_dct = {}
    buy, sell = [], []

    for i in range(len(req_id)):
        trans_id, rq_id = i, req_id[i]
        t, a, p = req_info[i]
        if rq_id not in trans_dct:
            trans_dct[rq_id] = [0, 0]

        if t:
            idx = bisect_left(buy, p)
            print(idx)
        else:
            idx = bisect_right(sell, p)
            print(idx)

        if t:
            sell.append((p, trans_id, rq_id, a))
            sell.sort()
        else:
            buy.append((p, trans_id, rq_id, a))
            buy.sort()

    # if 구매가격 >= sell_price:
    #     구매가격 가장 비싼 + 가장 먼저 들옥된

    #     -> buy amount -> 거래

    #     -> buy amount = buy, sellamount
    #     if not buy amount:
    #         done

    #     if not sell amount:
    #         done

    # else:
    #     pending

    return answer


print(
    solution(
        ["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"],
        [[1, 7, 20], [0, 10, 10], [1, 10, 40], [1, 4, 25], [0, 5, 11], [0, 20, 30]],
    )
)
