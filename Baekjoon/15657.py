from itertools import combinations_with_replacement

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

for per in combinations_with_replacement(lst, m):
    print(" ".join(map(str, per)))
