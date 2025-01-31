import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    
    # 종료 조건 : 온점이 입력되면 종료
    if sentence == '.':
        break

    # print("sentence: ", sentence)
    
    # 괄호들을 모아놓는 arr
    stack = []
    flag = True
    
    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            # 스택이 비어있거나 짝이 맞지 않는 경우
            if not stack or stack[-1] != '(':
                flag = False
                break
            stack.pop()
        elif char == ']':
            # 스택이 비어있거나 짝이 맞지 않는 경우
            if not stack or stack[-1] != '[':
                flag = False
                break
            stack.pop()
            
    if flag and not stack:
        print('yes')
    else:
        print("no")