import sys


def check_ancestor(duck: int):
    n = duck
    stop = 0
    while n != 1:
        if n in visited:
            stop = n
        n //= 2
    visited.add(duck)
    return stop


input = sys.stdin.readline
n, q = map(int, input().split())
visited = set()  # 중복방지

for _ in range(q):
    duck = int(input())
    print(check_ancestor(duck))
