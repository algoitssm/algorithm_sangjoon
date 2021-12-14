from collections import deque


def solution(progresses, speeds):
    answer = []
    prg = deque(progresses)
    spd = deque(speeds)
    t = 0

    while prg:
        temp = 0
        t += 1

        # 앞에서 부터 확인
        for i in range(len(prg)):
            if prg[i] + (spd[i] * t) >= 100:
                temp += 1
            else:
                break

        for i in range(temp):
            prg.popleft()
            spd.popleft()

        if temp:
            answer.append(temp)

    return answer
