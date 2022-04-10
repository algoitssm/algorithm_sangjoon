from collections import deque

n = int(input())
word = input()

lst = [0, 0, 0, 0]

for i in range(n):
    if word[i] == "W":
        lst[0] += 1

    if word[i] == "H":
        lst[1] += lst[0]

    if word[i] == "E":
        lst[3] += lst[3] + lst[2]
        lst[2] += lst[1]

print(lst[-1] % 1000000007)
