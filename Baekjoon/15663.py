from itertools import permutations

n, m = map(int, input().split())
lst = list(map(int, input().split()))

s = sorted(list(set(permutations(lst, m))))
for per in s:
    print(" ".join(map(str, per)))
