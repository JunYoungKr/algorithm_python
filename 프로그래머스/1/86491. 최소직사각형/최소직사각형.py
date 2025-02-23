def solution(sizes):
    answer = 0
    
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
            
    max_i = 0
    max_j = 0
    
    for i, j in sizes:
        if i > max_i:
            max_i = i
        if j > max_j:
            max_j = j
    answer = max_i * max_j
    return answer