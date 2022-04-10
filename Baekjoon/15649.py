def permutation(l):

    if len(l) == c:
        print(" ".join(l))
        return
    for i in range(1, n + 1):
        if not v[i]:
            v[i] = 1
            permutation(l + [str(i)])
            v[i] = 0


n, c = map(int, input().split())
v = [0] * (n + 1)
permutation([])
