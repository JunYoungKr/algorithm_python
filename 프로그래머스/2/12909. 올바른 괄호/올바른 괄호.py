def solution(s):
    answer = True
    
    stack = []
    
    for i in s:
        # 열린 괄호일 경우 stack에 넣어줌
        if i == '(' or not stack:
            stack.append(i)
        # 닫힌 괄호일 경우
        else:
            # stack[-1]이 '('인 경우
            if stack[-1] == '(' and i == ')':
                stack.pop()
        
        
    if stack:
        return False
    else:
        return True