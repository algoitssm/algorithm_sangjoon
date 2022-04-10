n = int(input())
lst = list(map(int, input().split()))
lst.sort()

if n % 2:
    n -= 1

i, max_m = 0, 0

while i < n // 2:
    m = lst[i] + lst[n - 1 - i]
    if m > max_m:
        max_m = m
    i += 1

print(max_m)
