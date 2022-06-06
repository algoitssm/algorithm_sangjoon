import sys


N, M = map(int, sys.stdin.readline().strip().split())

dct = {}

for _ in range(N):
    addr, pwd = sys.stdin.readline().strip().split()
    dct[addr] = pwd

for _ in range(M):
    addr = sys.stdin.readline().strip()
    print(dct[addr])
