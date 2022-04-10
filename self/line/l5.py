from collections import defaultdict


def solution(abilities, k):
    answer = 0
    l = len(abilities)
    ab = sorted(abilities, reverse=True)
    lst = []

    for i in range(0,l-1, 2):
        a, b = ab[i], ab[i+1]
        diff = a-b
        lst.append((diff, i))
        
    lst.sort(key = lambda x: (-x[0], x[1]))
    selected_lst = lst[:k]
    if l % 2 and ab[-1] > selected_lst[-1][0]:
        selected_lst.pop()
        answer += ab[-1]

    idx_lst = [idx for diff, idx in selected_lst]
    for i in range(0,l-1, 2):
        a, b = ab[i], ab[i+1]
        answer += a if i in idx_lst else b

    return answer


print(solution([2, 8, 3, 6, 1, 9, 1, 9]	, 2))
