from collections import deque

math_exp = deque(input())

ans = 0
add, sub = [], []
num = ""
start = True

while math_exp:
    e = math_exp.popleft()

    if start:  # - 연산자가 나오지 않았을 경우
        if e.isdigit():
            num += e
        else:
            add.append(int(num))
            num = ""
            if e == "-":
                start = False

    else:  # - 연산자 이후로 모두
        if e.isdigit():
            num += e
        else:
            sub.append(int(num))
            num = ""

if start:
    add.append(int(num))
else:
    sub.append(int(num))

ans = sum(add) - sum(sub)
print(ans)