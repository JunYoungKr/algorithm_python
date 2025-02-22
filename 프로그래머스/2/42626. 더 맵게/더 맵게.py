import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)  # 최소 힙으로 변환
    # print(scoville)
    
    while len(scoville) > 1 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new_scoville = first + second * 2
        heapq.heappush(scoville, new_scoville)
        answer += 1
    
    return answer if scoville[0] >= K else -1