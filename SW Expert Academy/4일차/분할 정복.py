import sys
input = sys.stdin.readline

# 병합 및 정렬
def merge_sort(arr):
    global count
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    # 왼쪽, 오른쪽으로 나눔
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 크다면 count 증가
    if left[-1] > right[-1]:
        count += 1
    
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    # 남은 원소 추가
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    number = list(map(int, input().split()))
    
    count = 0  # 오른쪽 원소가 먼저 복사되는 횟수 초기화
    sorted_arr = merge_sort(number)  # 병합 정렬 수행
    
    print(f'#{case} {sorted_arr[N//2]} {count}')  # 정렬된 중앙값과 카운트 출력
