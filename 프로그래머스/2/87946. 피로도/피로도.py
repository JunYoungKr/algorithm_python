from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    # 최대 탐험 가능한 던전 수
    max_count = 0
    
    # 현재 피로도 k
    # 각 던전별 "최소 필요 피로도, 소모 피로도"
    
    for perm in permutations(dungeons):
        피로도 = k
        count = 0
        
        # print(perm)
        
        for i, j in perm:
            # 현재 피로도 >= 최소 필요 피로도
            if 피로도 >= i:
                count += 1
                피로도 -= j
            else:
                break
        max_count = max(max_count, count)
    return max_count