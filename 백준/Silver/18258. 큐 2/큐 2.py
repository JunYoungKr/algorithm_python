import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
queue = deque([])

for _ in range(T):
    a = input().split()
    
    order = a[0]
    num = a[1] if len(a) > 1 else None
    
    # print("order, num: ", order, num)
    
    # push
    if order == 'push':
        queue.append(num)
    elif order == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
        