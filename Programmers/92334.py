from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    dic = defaultdict(set)
    cnt = defaultdict(int)

    for rep in report:
        s, e = rep.split()

        if e not in dic[s]:
            cnt[e] += 1

        dic[s].add(e)

    penalty_user = set()

    for key, value in cnt.items():
        if value >= k:
            penalty_user.add(key)

    for user in id_list:
        l = len(penalty_user.intersection(dic[user]))
        answer.append(l)

    return answer
