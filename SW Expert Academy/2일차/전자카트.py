import sys
input = sys.stdin.readline

# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
T = int(input())

# 다음 줄부터 테스트 케이스의 별로 첫 줄에 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 100이하의 자연수가 주어진다. 3<=N<=10
for case in range(T):
    # N 입력
    N = int(input())
    
    graph = [list(map(int, input().split(' '))) for _ in range(N)]
    
    # print(graph) -> 잘 입력됨
    
    
# 해결 못함