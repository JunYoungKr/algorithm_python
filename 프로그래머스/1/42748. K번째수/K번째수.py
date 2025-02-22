def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        # print(i, j, k)
        new_array = array[i-1:j]
        # print(new_array)
        new_array.sort()
        # print(new_array)
        answer.append(new_array[k-1])
        
    return answer