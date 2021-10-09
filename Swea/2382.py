# 211009 19:55
# 211009 21:08

class Microbe:

    """
    미생물에 대한 객체를 생성합니다.

    Attribultes:
        rc: 미생물의 위치
        size: 미생물의 크기
        d: 미생물의 방향

    Methods:
        move: 미생물을 이동 및 이동 위치 반환
        is_chemicals: 미생물의 위치가 약품인지 확인 및 화학처리
    """

    def __init__(self, r, c, cnt, d):
        self.rc = (r, c)
        self.size = cnt
        self.d = d

    def move(self):
        """
        기존의 이동방향으로 미생물을 이동 시킵니다.
        Returns:
            이동된 미생물의 위치를 반환합니다.
        """
        r, c = self.rc
        self.rc = (r + self.d[0], c + self.d[1])
        return self.rc

    def is_chemicals(self, n: int):  # 약품 충돌 확인
        """
        미생물의 위치가 약품구역인지 확인하고,
        맞을 경우 화학 처리를 진행합니다.

        Args: 
            n: 구역을 크기를 입력받습니다.
        Returns:
            True: 약품구역의 해당여부를 판단
        """
        r, c = self.rc
        if r == 0 or r == n-1 or c == 0 or c == n-1:
            d1, d2 = self.d
            self.d = (-d1, -d2)
            self.size //= 2
            return True

        return False


ans = []
test = int(input())
for tc in range(1, test+1):
    n, m, k = map(int, input().split())
    nd = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
    micorbes = dict()
    p = []
    res = 0

    for i in range(k):  # 미생물 객체를 생성합니다.
        r, c, cnt, d = map(int, input().split())
        micorbes[i] = Microbe(r, c, cnt, nd[d])

    for _ in range(m):
        visited = dict()  # 방문표시를 초기화합니다.
        for idx, mic in micorbes.items():  # 모든 미생물을 이동 시킵니다.
            r, c = mic.move()
            mic.is_chemicals(n)  # 화학처리 확인 및 진행합니다.
            if (r, c) in visited:  # 방문처리합니다.
                visited[(r, c)].append(idx)
            else:
                visited[(r, c)] = [idx]

        for _, idxs in visited.items():
            if len(idxs) > 1:  # 동일 구역에 여러 미생물이 위치할 경우
                sum_size = 0
                max_size = max_idx = max_mic = 0
                for idx in idxs:  # 순회하며, 최대 미생물 객체를 반환
                    mic = micorbes.pop(idx)
                    sum_size += mic.size
                    if mic.size >= max_size:
                        max_size = mic.size
                        max_mic = mic
                        max_idx = idx
                max_mic.size = sum_size  # 미생물의 크기를 수정
                micorbes[max_idx] = max_mic

    for idx, mic in micorbes.items():
        res += mic.size

    ans.append("#{} {}".format(tc, res))

print(*ans, sep="\n")
