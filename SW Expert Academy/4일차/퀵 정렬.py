import sys
input = sys.stdin.readline

def quick_sort(arr, start, end):
    
    # 원소가 1개인 경우 바로 종료
    if start >= end:
        return
    
    # pivot은 첫 번째 원소
    pivot = start
    left = start + 1
    right = end
    
    while (left <= right):
        # pivot보다 큰 데이터를 찾을 때까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # pivot보다 작은 데이터를 찾을 때까지 반복
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        # 엇갈린 경우 작은 데이터와 피봇을 교체
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    
    arr = list(map(int, input().split()))
    
    quick_sort(arr, 0, len(arr) - 1)
    
    print("#{} {}".format(case, arr[N//2]))
    
    
# 7 5 4 1 2 10 3 6 9 8	