def solution(stones, k):
    s, e = 0, max(stones)

    while s <= e:
        tmp = 0
        m = (s + e) // 2

        for s in stones:
            if s - m <= 0:
                tmp += 1
            else:
                tmp = 0

            if tmp >= k:
                break

        if tmp < k:
            s = m + 1
        else:
            answer = m
            e = m - 1

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 1))
