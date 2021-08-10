n = int(input())
lst = list(map(int, input().split()))
lst.sort()

ans_lst = [0]

for time in lst:
    ans_lst.append(time + ans_lst[-1])

print(sum(ans_lst))
