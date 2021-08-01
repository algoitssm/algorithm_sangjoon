n = int(input())
check = ["3", "6", "9"]
for i in range(1, n + 1):
    cnt = 0
    for num in str(i):
        if num in check:
            cnt += 1
    if cnt:
        print("-" * cnt, end=" ")
    else:
        print(i, end=" ")
