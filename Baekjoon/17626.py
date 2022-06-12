n = int(input())

d= [0 for _ in range(n+1)]
d[1] = 1

for  i in range(2, n+2):
    min_val = 1e9
    j = 1
    while j**2  <= 1:
        min_val = min(min_val, d[i-(j**2)])
        j += 1

    d[i] = min_val + 1
