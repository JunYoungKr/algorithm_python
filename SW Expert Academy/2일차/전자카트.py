import sys
input = sys.stdin.readline

# N개의 컨테이너를 M대의 트럭으로 A도시 -> B도시로 운반
# 트럭 당 한 개의 컨테이너를 운반할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.
# A->B 도시로 최대 M대의 트럭이 편도로 한 번만 운행
# 이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인가

# 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.

# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
T = int(input())


for case in range(T):
    # 컨테이너 수 N, 트럭 수 M이 주어짐
    N, M = map(int, input().split(' '))
    
    # N개의 화물의 무게 w
    w = list(map(int, input().split(' ')))
    
    # M개의 트럭의 적재용량 t
    t = list(map(int, input().split(' ')))
    
    w.sort(reverse=True)
    # print(w)
    
    t.sort(reverse=True)
    # print(t)
    
    # 총 무게
    total_weight = 0
    
    used = [False] * N  # 화물 사용 여부 추적

    # used 배열을 사용하여 solved한 코드
    
    # 적재용량이 큰 트럭부터 순회
    # for truck in t:
    #     for i in range(N):
    #         if not used[i] and truck >= w[i]:
    #             total_weight += w[i]
    #             used[i] = True  # 해당 화물 사용 처리
    #             break  # 하나의 트럭에는 하나의 화물만 적재 가능

    # print(f"#{case+1} {total_weight}")
                
    # 화물을 제거하여 solved한 코드
    
    for truck in t:
        for i in range(len(w)):
            if truck >= w[i]:
                total_weight += w[i]
                w.pop(i)  # 해당 화물 제거
                break  # 하나의 트럭에는 하나의 화물만 적재 가능

    print(f"#{case+1} {total_weight}")

