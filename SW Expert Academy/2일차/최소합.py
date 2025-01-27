# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
T = int(input())


for case in range(T):
    
    
    # 다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13
    N = int(input())
    
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    # print(graph, end='\n')
    
    # 정답 도출 (초기값 더해놓음)
    result = graph[0][0]
    
    dp = [[0] * N for _ in range(N)]
    
    # dp 가로, 세로 줄 더해줌
    for i in range(N):
        dp[0][i] = dp[0][i-1] + graph[0][i]
        dp[i][0] = dp[i-1][0] + graph[i][0]
    
    # print(dp)
    
    # dp 비교하며 시작
    for i in range(1, N):
        for j in range(1, N):
            if dp[i-1][j] + graph[i][j] < dp[i][j-1] + graph[i][j]:
                dp[i][j] = dp[i-1][j] + graph[i][j]
            else:
                dp[i][j] = dp[i][j-1] + graph[i][j]
    
    # for i in range(N):
    #     for j in range(N):
    #         print(dp[i][j], end=' ')
    #     print('\n')
    
    print("#{} {}".format(case+1, dp[N-1][N-1]))
    