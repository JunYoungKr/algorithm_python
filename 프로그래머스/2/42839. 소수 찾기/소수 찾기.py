from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    
    array = set()
    for perm in range(1, len(numbers) + 1):
        for i in permutations(numbers, perm):
            num = int(''.join(i))
            array.add(num)
    print(array)
    
    return sum(1 for num in array if is_prime(num))
