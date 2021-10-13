from itertools import combinations_with_replacement

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

s = sorted(list(set(combinations_with_replacement(lst, m))))
for per in s:
    print(" ".join(map(str, per)))
