from itertools import combinations

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

for com in combinations(lst, m):
    print(" ".join(map(str, com)))
