def solution(N, stages):
    answer = []
    cnt = {i + 1: 0 for i in range(N)}
    dic = {}
    l = len(stages)

    for stage in stages:
        if stage in cnt.keys():
            cnt[stage] += 1

    for k, v in cnt.items():
        dic[k] = v / l if l != 0 else 0
        l -= v

    tmp = list(sorted(dic.items(), key=lambda x: (-x[1], x[0])))

    for t in tmp:
        answer.append(t[0])

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
