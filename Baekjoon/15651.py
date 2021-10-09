def permutation_repeat(m, lst):
    if m == 0:
        print(" ".join(map(str, lst)))
        return
    for i in range(1, n+1):
        permutation_repeat(m-1, lst+[i])


n, m = map(int, input().split())
permutation_repeat(m, [])
