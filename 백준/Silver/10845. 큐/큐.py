import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque([])
for _ in range(N):
    i = input().split()
    order = i[0]
    num = i[1] if len(i) > 1 else None
    # print(order, num)
    # push X: 정수 X를 큐에 넣는 연산이다.
    if order == 'push':
        queue.append(num)
    # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif order == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    # size: 큐에 들어있는 정수의 개수를 출력한다.
    elif order == 'size':
        print(len(queue))
    # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    elif order == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif order == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif order == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)