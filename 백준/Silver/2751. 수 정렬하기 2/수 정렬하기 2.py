import sys
input = sys.stdin.readline
print = sys.stdout.write  # 빠른 출력 사용

# 입력
N = int(input())
array = [int(input()) for _ in range(N)]

# 정렬
array.sort()

# 출력
for num in array:
    print(f"{num}\n")
