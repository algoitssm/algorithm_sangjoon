N = int(input())

t, f, x = 0, 0, 0

for i in range(1, N + 1):
    while i // 10 and not i % 10:
        i /= 10
        x += 1

    while i // 5 and not i % 5:
        i /= 5
        f += 1

    while i // 2 and not i % 2:
        i /= 5
        t += 1

answer = x + min(t, f)
print(answer)
