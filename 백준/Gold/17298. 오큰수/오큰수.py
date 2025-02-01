import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 정답 배열을 -1로 초기화 (오큰수가 없는 경우 -1)
answer = [-1] * N
stack = []  # 단조 스택

# 오른쪽에서 왼쪽으로 탐색
for i in range(N - 1, -1, -1):
    # 스택에 있는 값들 중 현재 A[i]보다 작거나 같은 값은 필요 없으므로 제거
    while stack and stack[-1] <= A[i]:
        stack.pop()
    # 스택에 값이 있다면, 스택의 top이 A[i]의 오큰수
    if stack:
        answer[i] = stack[-1]
    # 현재 값을 스택에 추가
    stack.append(A[i])
    
# 정답 출력 (공백으로 구분하여 한 줄에 출력)
print(' '.join(map(str, answer)))
