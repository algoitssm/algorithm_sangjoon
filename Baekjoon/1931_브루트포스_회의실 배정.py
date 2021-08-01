import sys


input = sys.stdin.readline

n = int(input())
lst = [(tuple(map(int, input().split()))) for _ in range(n)]
lst.sort(key=lambda x: (x[1], x[0]))

start, cnt = 0, 0

for time in lst:
    if time[0] >= start:
        start = time[1]
        cnt += 1

print(cnt)