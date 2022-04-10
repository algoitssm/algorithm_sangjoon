def dfs(idx, cal):
    global max_v
    global min_v

    if idx >= n:
        min_v = min(min_v, cal)
        max_v = max(max_v, cal)
        return

    for i in range(4):
        if op[i]:
            op[i] -= 1
            temp = cal
            if i == 0:
                temp += nums[idx]
            if i == 1:
                temp -= nums[idx]
            if i == 2:
                temp *= nums[idx]
            if i == 3:
                temp /= nums[idx]
            dfs(idx + 1, int(temp))
            op[i] += 1


test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    op = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    operator = ["+", "-", "*", "/"]
    min_v, max_v = 100000000, -100000000

    dfs(1, nums[0])
    ans = max_v - min_v

    print(f"#{test} {ans}")
