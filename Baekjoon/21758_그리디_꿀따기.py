import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

# 중간에 벌꿀통이 있을 경우
lst_mid = lst[1:-1]
max_sum = sum(lst_mid) + max(lst_mid)

# 한쪽 끝에 벌통이 있을 경우
for i in range(1, n):
    temp_sum_left = sum(lst[1:i] + lst[i + 1 :] * 2)
    temp_sum_right = sum(lst[:i] * 2 + lst[i + 1 :])
    print(lst[:i], lst[i + 1 :])
    print(temp_sum_left, temp_sum_right)
    max_sum = max(max_sum, temp_sum_left, temp_sum_right)

print(max_sum)