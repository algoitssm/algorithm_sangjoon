def permutation(m, lst):
    if m == 0:
        print(" ".join(map(str, lst)))
        return

    for i in range(n):
        if not v[i]:
            v[i] = 1
            permutation(m-1, lst+[l[i]])
            v[i] = 0


n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
v = [0]*n
permutation(m, [])
