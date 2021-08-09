def check_change(n: int):
    if n in [1, 3]:
        return -1

    five, mod = divmod(n, 5)

    if mod % 2:
        five -= 1
        two = (mod + 5) // 2
    else:
        two = mod // 2

    return five + two


n = int(input())
ans = check_change(n)
print(ans)