n = int(input())
path = list(map(int, input().split()))
charge = list(map(int, input().split()))

ans, pay = 0, charge[0]

for i in range(n - 1):
    if charge[i] < pay:
        pay = charge[i]
    ans += pay * path[i]

print(ans)


# charge = charge[:-1]
# ans, idx = 0,n

# while idx > 0:
#     min_c = min(charge)
#     idx = charge.index(min_c)

#     ans += min_c * sum(path[idx:])
#     path, charge = path[:idx], charge[:idx]
