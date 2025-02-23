def solution(answers):
    answer = []
    
    # 1번 수포자 : 1 2 3 4 5
    # 2번 수포자 : 2 1 2 3 2 4 2 5
    # 3번 수포자 : 3 3 1 1 2 2 4 4 5 5
    
    number_1 = [1, 2, 3, 4, 5]
    number_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    number_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    count_1 = 0
    count_2 = 0
    count_3 = 0
    
    count = [0, 0, 0]
    
    # 문제의 길이에 맞게 수포자 패턴을 순환 (mod 연산 활용)
    for i, ans in enumerate(answers):
        # 1번 수포자
        if ans == number_1[i % len(number_1)]:
            count[0] += 1
        
        # 2번 수포자
        if ans == number_2[i % len(number_2)]:
            count[1] += 1
        
        # 3번 수포자
        if ans == number_3[i % len(number_3)]:
            count[2] += 1
    
    # 가장 높은 점수를 받은 수포자 찾기
    max_score = max(count)  # 가장 많이 맞힌 점수
    # print("max_score: ", max_score)
    answer = []
    
    # count[i]가 max_score랑 같은 모든 i에 대해 (i+1)을 결과에 추가
    for i, c in enumerate(count):
        if c == max_score:
            answer.append(i+1)  # 수포자 번호는 인덱스+1
    
    return answer