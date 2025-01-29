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
        
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
            
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    
    arr = list(map(int, input().split()))
    
    quick_sort(arr, 0, len(arr) - 1)
    
    print("#{} {}".format(case, arr[N//2]))
    
    
# 7 5 4 1 2 10 3 6 9 8	