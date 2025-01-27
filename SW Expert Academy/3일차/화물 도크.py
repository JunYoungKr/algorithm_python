import sys

input = sys.stdin.readline

# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
T = int(input())

for case in range(T):
    # 다음 줄부터 테스트 케이스의 별로 첫 줄에 신청서 N이 주어지고
    N = int(input())
    
    time = []
    
    for case2 in range(N):
        # 다음 줄부터 N개의 줄에 걸쳐 화물차의 작업 시작 시간 s와 종료 시간 e가 주어진다.
        time.append(list(map(int, input().split(' '))))
    
    # 오름차순 정렬
    time.sort(key=lambda x:x[1])
    
    count = 0
    finished_time = 0
    
    for start, end in time:
        if start >= finished_time:
            count += 1
            finished_time = end
        
    
    print("#{} {}".format(case+1, count))