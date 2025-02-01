import sys
input = sys.stdin.readline

# 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.

n = int(input().strip())

arr = [i for i in range(1, n + 1)]

num = 1
stack = []
answer = []
flag = True

for i in range(n):
    a = int(input())
    while num <= a:
        stack.append(num)
        num += 1
        answer.append("+")
        
    if stack[-1] == a:
        stack.pop()
        answer.append("-")
    else:
        flag = False
        break
    
if not flag:
    print("NO")
else:
    for i in answer:
        print(i, end='\n')