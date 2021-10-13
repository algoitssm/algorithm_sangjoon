from itertools import combinations

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

s = sorted(list(set(combinations(lst, m))))
for per in s:
    print(" ".join(map(str, per)))
