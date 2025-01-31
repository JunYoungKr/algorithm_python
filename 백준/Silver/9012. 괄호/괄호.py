import sys
input = sys.stdin.readline

N = int(input())


for _ in range(N):
    a = input().strip()
   
    a = list(a)
    # print(a)
   
    stack = []
    for i in a:
       # 열린 괄호면 stack.append
       if len(stack) == 0 or i == '(':
           stack.append(i)
       # stack[-1]이 열린 괄호고 현재 요소가 닫힌 괄호라면 stack.pop()
       elif stack[-1] == '(' and i == ')':
           stack.pop()
           
    if stack:
        print("NO")
    else:
        print("YES")
   