from sys import stdin

input = stdin.readline
test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())

    for _ in range(m):
        a, b = map(int, input().split())

    # 최소 이동거리는 트리의 간선 개수
    print(n - 1)
