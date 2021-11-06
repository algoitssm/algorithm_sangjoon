def check_out(r, c):
    if 0 <= r < n or 0 <= c < n:
        return 1
    return 0


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    mp = []

    res = [0]

    ans.append("#{} {}".format(test, res))

print(*ans, sep="\n")
