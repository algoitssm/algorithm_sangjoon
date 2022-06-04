N = int(input())
M = int(input())
error_set = set()

if M:
    error_set = set(map(int, input().split()))


ans = abs(100 - N)

for num in range(1000001):
    for n in str(num):
        if int(n) in error_set:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - N))

print(ans)
