from itertools import product

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

s = sorted(list(set(product(lst, repeat=m))))
for per in s:
    print(" ".join(map(str, per)))
