def solution(brown, yellow):
    answer = []
    
    # 카펫의 크기는 결국 brown + yellow
    carpet = brown + yellow
    # print(carpet)
    
    array = []
    
    # 12라면 (1, 12), (2, 6), (3, 4), (4, 3), (6, 2), (12, 1)
    for i in range(1, carpet+1):
        if carpet % i == 0 and i >= carpet // i:
            array.append([i, carpet // i])
            
    for i, j in array:
        print(i, j)
        if yellow == (i-2)*(j-2):
            return [i, j]
