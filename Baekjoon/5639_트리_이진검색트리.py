def postorder_traverse(s: int, e: int):
    # 자식 노드가 없는 경우
    if s > e:
        return

    # 끝점 초기화
    mid = e + 1

    # 오른쪽 노드 지점 탐색
    for i in range(s + 1, e + 1):
        if lst[s] < lst[i]:
            mid = i
            break

    # 왼쪽 노드 탐색
    postorder_traverse(s + 1, mid - 1)
    # 오른쪽 노드 탐색
    postorder_traverse(mid, e)
    print(lst[s])


import sys


sys.setrecursionlimit(10 ** 9)

lst = []
cnt = 0

while cnt <= 10000:
    try:
        lst.append(int(input()))

    except:
        break

    cnt += 1

postorder_traverse(0, len(lst) - 1)
