def recursive_power(n, r, c):
    l = 2**(n-1)
    if n == 0:
        return 0

    if r < l and c < l:
        return 0 * l**2 + recursive_power(n-1, r % l, c % l)
    elif r < l and c >= l:
        return 1 * l**2 + recursive_power(n-1, r % l, c % l)
    elif r >= l and c < l:
        return 2 * l**2 + recursive_power(n-1, r % l, c % l)
    elif r >= l and c >= l:
        return 3 * l**2 + recursive_power(n-1, r % l, c % l)


N, r, c = map(int, input().split())
print(recursive_power(N, r, c))
