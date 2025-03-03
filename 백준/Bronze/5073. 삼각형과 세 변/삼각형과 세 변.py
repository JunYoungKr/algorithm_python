import sys
input = sys.stdin.readline


# 가장 긴 변의 길이 > 나머지 두 변의 길이의 합 -> invalid 출력

while True:
    num = list(map(int, input().split(' ')))
    num.sort(reverse=True)
    # print(a, b, c)
    # print(num)
    # 종료 조건
    if num == [0, 0, 0]:
        break
    
    # 삼각형의 조건을 만족하지 못하는 경우
    if num[0] >= num[1] + num[2]:
        print("Invalid")
    
    # 세 변의 길이가 모두 같은 경우
    elif num[0] == num[1] == num[2]:
        print("Equilateral")
        
    # 두 변의 길이만 같은 경우
    elif num[0] == num[1] or num[1] == num[2]:  
        print("Isosceles")
    
    # 세 변의 길이가 모두 다른 경우
    else:
        print("Scalene")