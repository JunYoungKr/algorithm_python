def solution(arr):
    answer = []
    
    # 연속임을 세주는 count
    count = [0 for _ in range(len(arr))]

    
    for i in range(len(arr)-1):
        # 다음 요소와 같다면
        if arr[i] == arr[i+1]:
            count[i+1] += 1
    
    for idx, flag in enumerate(count):
        if flag == 0:
            answer.append(arr[idx])
            
    return answer