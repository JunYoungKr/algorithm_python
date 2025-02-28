def solution(nums):
    answer = 0
    
    length = len(nums)
    nums = set(nums)
    
    print(length)
    
    if len(nums) >= length // 2:
        return length // 2
    else:
        return len(nums)
     