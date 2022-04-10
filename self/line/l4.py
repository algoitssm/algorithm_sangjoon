def solution(arr, brr):
    answer = 0
    for i in range(len(arr) - 1):
        if arr[i] == brr[i]:
            continue
        answer += 1
        diff = brr[i] - arr[i]
        arr[i + 1] -= diff

    return answer


print(solution([3, 7, 2, 4], [4, 5, 5, 2]))
print(solution([6, 2, 2, 6], [4, 4, 4, 4]))
