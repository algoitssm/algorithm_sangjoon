n = int(input())
lst = [1, 2]

for i in range(2, n):
    lst.append((lst[i - 2] + lst[i - 1]) % 10007)

print(lst[n - 1])
