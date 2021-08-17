n = int(input())
lst = list(input())

R, B = 0, 0
last = ""

while lst:  # 한 개씩 출력 연속된 그룹 개수 측정
    e = lst.pop()

    if e != last:  # 색상 변화지점 체크
        last = e
        if e == "R":
            R += 1
        else:
            B += 1

ans = min(R, B) + 1  # 최소그룹제외 한가지 색으로 색칠

print(ans)
