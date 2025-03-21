import sys
input = sys.stdin.readline

# 테스트 케이스 P
P = int(input())

for case in range(P):
    # 테스트 케이스 T와 20개의 양의 정수가 공백으로 구분되어 주어짐 -> 총 21개의 정수 입력
    num = list(map(int, input().split()))
    
    # print(num)
    # num의 첫 번째 요소는 테스트 케이스
    # i = 1번째부터는 학생들의 키
    testcase = num[0]
    heights = num[1:]
    
    queue = []
    count = 0
    
    for height in heights:
        pos = 0
        
        # 현재 queue에 있는 학생들 중 자신보다 큰 사람 찾기
        while pos < len(queue) and queue[pos] < height:
            pos += 1
            
        # 자리를 찾았으면 삽입
        queue.insert(pos, height)
        # 삽입할 때 지나친 학생 수를 count에 더함
        count += len(queue) - pos - 1
    print(testcase, count)
        
        
    