from collections import Counter

def solution(participant, completion):
    answer = ''
    result = list(Counter(participant)-Counter(completion))
    
    print(result[0])
    return result[0]