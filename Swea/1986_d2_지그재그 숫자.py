test = int(input())

for t in range(1, test + 1):
    n = int(input())
    ans = 0
    for i in range(n + 1):
        ans += i if i % 2 else i * (-1)
    print(f"#{t} {ans}")
