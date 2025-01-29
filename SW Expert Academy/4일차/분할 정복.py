import sys
input = sys.stdin.readline

# 🔍 이진 탐색 함수 (탐색 방향 변경 체크)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    prev_direction = None  # 이전 방향 저장 (None, 'left', 'right')
    found = False

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True  # 찾으면 방향 상관없이 정답

        if arr[mid] > target:  # 왼쪽 탐색
            if prev_direction == "right":
                found = True  # 방향 변경 감지
            right = mid - 1
            prev_direction = "left"
        else:  # 오른쪽 탐색
            if prev_direction == "left":
                found = True  # 방향 변경 감지
            left = mid + 1
            prev_direction = "right"
    
    return found  # 방향 변경이 발생한 경우 True, 아니면 False

# 🔥 메인 실행 코드
T = int(input().strip())  # 테스트 케이스 개수

for case in range(1, T + 1):
    # 입력 받기
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))  # A 리스트 정렬
    B = list(map(int, input().split()))  # B 리스트

    # B의 각 원소를 A에서 이진 탐색하면서 조건을 만족하는 개수 찾기
    count = sum(1 for num in B if binary_search(A, num))

    print(f"#{case} {count}")  # 결과 출력
