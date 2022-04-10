def combination(idx, l):

    if len(l) == c:
        print(" ".join(l))
        return

    for i in range(idx, n + 1):
        combination(idx + 1, l + [str(i)])


n, c = map(int, input().split())
