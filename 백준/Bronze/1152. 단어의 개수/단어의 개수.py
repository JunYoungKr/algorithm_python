import sys
input = sys.stdin.readline

# 입력
a = input().strip()

# 스택 선언
stack = []

count = 0

# 문자열 순회
for char in a:
    # 공백이 아닌 문자가 나올 경우 스택에 push
    if char != ' ':
        stack.append(char)
        # print(stack)
    
    # 공백이 나왔을 때 스택에 단어가 있다면 단어 하나로 간주
    elif stack:
        count += 1
        stack.clear() # 스택 비우기
        
# print(stack)

if stack:
    count += 1
    
print(count)