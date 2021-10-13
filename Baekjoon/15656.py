from itertools import product

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

for per in product(lst, repeat=m):
    print(" ".join(map(str, per)))
