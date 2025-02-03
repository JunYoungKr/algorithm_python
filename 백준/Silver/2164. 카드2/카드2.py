import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

arr = deque(i for i in range(1, N+1))
# print(arr)

while len(arr) > 1:
    # 제일 위에 있는 카드를 버림
    arr.popleft()
    # 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮김
    num = arr.popleft()
    arr.append(num)

print(arr[0])