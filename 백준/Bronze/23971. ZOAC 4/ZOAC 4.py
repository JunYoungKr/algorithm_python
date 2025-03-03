import sys
input = sys.stdin.readline


# H, W, N, M이 공백으로 구분되어 주어진다. (0 < H, W, N, M ≤ 50,000)
N, M, R, C = map(int, input().split(' '))
a = ((N + (R + 1) - 1) // (R + 1))
b = ((M + (C + 1) - 1) // (C + 1))

print(a * b)