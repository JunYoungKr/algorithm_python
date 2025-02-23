import math

def solution(progresses, speeds):
    answer = []
    time = []
    stack = []
    
    for i in range(len(progresses)):
        time.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    # print(time) # 7, 3, 9
    
    stack.append(time.pop(0))
    current = stack[0]
    while time:
        print(time)
        if current >= time[0]:
            stack.append(time.pop(0))
        else:
            answer.append(len(stack))
            current = time[0]
            stack.clear()
            # break
    answer.append(len(stack))
    return answer