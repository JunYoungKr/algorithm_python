import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    
    stack = deque()
    
    for i in range(len(progresses)):
        stack.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    #
    while stack:
        # 첫 번째 뺌
        deploy_day = stack.popleft()
        count = 1
        
        while stack and stack[0] <= deploy_day:
            stack.popleft()
            count += 1
        
        answer.append(count)
        count = 1
    
    return answer

