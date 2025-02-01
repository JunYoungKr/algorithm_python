import sys
input = sys.stdin.readline

# 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.

K = int(input())

stack = []

for _ in range(K):
    N = int(input())
    
    if N == 0:
        stack.pop()
    else:
        stack.append(N)
    
    # print("stack: ", stack)

print(sum(stack))