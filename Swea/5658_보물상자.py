# 5분


class Lock:
    def __init__(self, lock: list, total_length: int):
        self.lock = lock
        self.total_length = total_length

    def rotate(self):
        last = self.lock.pop()
        self.lock = [last] + self.lock

    def get_password_lst(self):
        password_lst = set()
        lock_length = self.total_length // 4
        # 회전
        for _ in range(lock_length):
            self.rotate()
            # 비밀번호 입력
            for i in range(0, self.total_length, lock_length):
                password = "".join(self.lock[i : i + lock_length])
                password_lst.add(int(password, 16))

        return sorted(password_lst, reverse=True)


test = int(input())

for test_case in range(1, test + 1):
    N, K = map(int, input().split())
    lock = list(input())
    lock = Lock(lock, N)
    password_lst = lock.get_password_lst()
    ans = password_lst[K - 1]
    print(f"#{test_case} {ans}")
