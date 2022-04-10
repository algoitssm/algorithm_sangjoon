from collections import deque
from sys import stdin


def get_ancestor(a: int, b: int):
    dq = deque([a, b])
    visited = [a, b]  # 방문 부모노드 체크

    while dq:
        e = dq.popleft()

        for node in tr[e]:
            if node in visited:
                return node
            visited.append(node)
            dq.append(node)


input = stdin.readline

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    tr = [[] for _ in range(n + 1)]  # 부모노드 기록하는 리스트 생성

    for _ in range(n - 1):
        a, b = map(int, input().split())
        tr[b].append(a)

    a, b = map(int, input().split())
    print(get_ancestor(a, b))
