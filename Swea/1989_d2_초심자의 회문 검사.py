from collections import deque


def is_pelindrome(text: str):
    dq = deque(text)
    while len(dq) > 1:
        right = dq.pop()
        left = dq.popleft()
        if right != left:
            return 0
    return 1


t = int(input())

for test in range(1, t + 1):
    text = input()
    ans = is_pelindrome(text)
    print(f"#{test} {ans}")
