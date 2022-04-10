import heapq


def sync(que):
    while que and not lst[que[0][1]]:
        heapq.heappop(que)


test_case = int(input())
for _ in range(test_case):
    k = int(input())
    max_q, min_q = [], []
    lst = [0] * 1000001

    for i in range(k):
        d, n = input().split()

        if d == "I":
            heapq.heappush(max_q, (-int(n), i))
            heapq.heappush(min_q, (int(n), i))
            lst[i] = 1

        elif n == "1":
            sync(max_q)

            if max_q:
                lst[max_q[0][1]] = 0
                heapq.heappop(max_q)
        else:
            sync(min_q)

            if min_q:
                lst[min_q[0][1]] = 0
                heapq.heappop(min_q)

    sync(max_q)
    sync(min_q)

    if max_q and min_q:
        print(-max_q[0][0], min_q[0][0])
    else:
        print("EMPTY")
