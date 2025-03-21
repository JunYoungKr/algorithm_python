import sys
input = sys.stdin.readline

# 국가의 수 N, 등수를 알고 싶은 국가 K
N, K = map(int, input().split())

arr = []

for i in range(N):
    # 국가를 나타내는 정수와 금, 은, 동메달의 수가 빈칸을 사이에 두고 주어짐
    arr.append(list(map(int, input().split())))

# 금, 은, 동 내림차순 정렬
arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1  # 현재 등수
for i in range(N):
    if i > 0 and arr[i][1:] == arr[i-1][1:]:
        # 동점이면 등수 유지
        pass
    else:
        # 새로운 등수로 갱신
        rank = i + 1

    if arr[i][0] == K:
        print(rank)
        break
