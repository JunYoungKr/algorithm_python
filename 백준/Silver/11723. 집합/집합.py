import sys
input = sys.stdin.readline

N = int(input())
S = set()  # 리스트 대신 set 사용

for _ in range(N):
    command = input().strip().split()
    
    if command[0] == 'add':
        S.add(int(command[1]))  # add 연산

    elif command[0] == 'remove':
        S.discard(int(command[1]))  # remove는 discard 사용 (없는 경우 예외 방지)

    elif command[0] == 'check':
        print(1 if int(command[1]) in S else 0)  # check 연산

    elif command[0] == 'toggle':
        num = int(command[1])
        if num in S:
            S.remove(num)  # 있으면 제거
        else:
            S.add(num)  # 없으면 추가

    elif command[0] == 'all':
        S = set(range(1, 21))  # {1, 2, ..., 20}으로 변경

    elif command[0] == 'empty':
        S.clear()  # 공집합으로 변경
