test = int(input())
rank_lst = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for t in range(1, test + 1):
    n, k = map(int, input().split())
    lst = [[i] + list(map(int, input().split())) for i in range(1, n + 1)]
    lst.sort(key=lambda x: (x[1] * 35 + x[2] * 45 + x[3] * 20), reverse=True)

    for rank, student_desc in enumerate(lst, start=1):
        if student_desc[0] == k:
            score = rank_lst[(rank - 1) * 10 // n]
            print(f"#{t} {score}")