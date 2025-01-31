import sys
input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    a = input().strip().split(' ')
    
   # 명령어와 인수 분리
    order = a[0]
    num = a[1] if len(a) > 1 else None  # num은 push일 때만 존재
    # print("order, num: ", order, num)
    
    if order == 'push':
        stack.append(int(num))
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])