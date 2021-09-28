from collections import deque


class Magnet:
    #########################
    #   시계에 대한 객체 생성    #
    #########################
    def __init__(self, magnet, num):
        self.magnet = deque(magnet)
        self.num = num

    def rotate(self, clockwise):
        if clockwise == 1:
            e = self.magnet.pop()
            self.magnet.appendleft(e)
        if clockwise == -1:
            e = self.magnet.popleft()
            self.magnet.append(e)


def find_magnet_left(n):
    if n > 0:
        if m[n].magnet[6] != m[n-1].magnet[2]:
            rotate_magnet.append(n-1)
            find_magnet_left(n-1)


def find_magnet_right(n):
    if n < 3:
        if m[n].magnet[2] != m[n+1].magnet[6]:
            rotate_magnet.append(n+1)
            find_magnet_right(n+1)


test_case = int(input())

for test in range(1, test_case+1):
    k = int(input())
    m = [Magnet(list(map(int, input().split())), i) for i in range(1, 5)]
    ans = 0

    for _ in range(k):
        n, d = map(int, input().split())
        n -= 1

        rotate_magnet = [n]
        find_magnet_left(n)  # 우측 자석 탐색
        find_magnet_right(n)  # 좌측 자석 탐색

        for magnet in rotate_magnet:  # 회전가능 자석에 대해 회전 수행
            if (n-magnet) % 2:
                m[magnet].rotate(d*(-1))
            else:
                m[magnet].rotate(d)

    for i in range(4):
        if m[i].magnet[0] == 1:
            ans += 2**i

    print(f"#{test} {ans}")
