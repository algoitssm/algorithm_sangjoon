n = int(input())

ans = 0
ropes = [int(input()) for _ in range(n)]
ropes.sort()

for i in range(n):
    max_weight = ropes[i] * (n - i)
    if max_weight > ans:
        ans = max_weight

print(ans)
