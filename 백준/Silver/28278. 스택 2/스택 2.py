import sys
input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    i = input().strip().split()
    
    order = int(i[0])
    num = i[1] if len(i) > 1 else None
    
    # print(order, num)
    
    # 1 X
    if order == 1:
        stack.append(num)
    # 2
    elif order == 2:
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    # 3
    elif order == 3:
        print(len(stack))
    # 4
    elif order == 4:
        if stack:
            print(0)
        else:
            print(1)
    # 5
    elif order == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
    