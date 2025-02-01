import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))

# 스택과 정답 배열 초기화
stack = []
answer = [0] * N

# 오른쪽에서 왼쪽으로 순회
for i in range(N-1, -1, -1):
    # 현재 탑보다 낮은 탑들은 스택에서 제거
    while stack and tower[stack[-1]] < tower[i]:
        answer[stack.pop()] = i + 1
    # 현재 탑을 스택에 추가
    stack.append(i)

print(" ".join(map(str, answer)))
