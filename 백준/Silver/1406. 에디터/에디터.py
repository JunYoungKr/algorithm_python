import sys
input = sys.stdin.readline

# 초기 문자열과 명령어 수 입력
a = input().strip()
N = int(input())

# 두 개의 스택으로 문자열 관리
left_stack = list(a)       # 커서 왼쪽 문자열
right_stack = []           # 커서 오른쪽 문자열

# 명령어 처리
for _ in range(N):
    command = input().strip().split()

    if command[0] == 'L':  # 커서를 왼쪽으로 이동
        if left_stack:
            right_stack.append(left_stack.pop())

    elif command[0] == 'D':  # 커서를 오른쪽으로 이동
        if right_stack:
            left_stack.append(right_stack.pop())

    elif command[0] == 'B':  # 커서 왼쪽 문자 삭제
        if left_stack:
            left_stack.pop()

    elif command[0] == 'P':  # 커서 왼쪽에 문자 추가
        left_stack.append(command[1])

# 결과 출력
# 왼쪽 스택과 오른쪽 스택을 합쳐서 출력
print(''.join(left_stack + right_stack[::-1]))
