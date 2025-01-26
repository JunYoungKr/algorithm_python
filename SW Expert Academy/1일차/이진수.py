# [입력]

# 다음 줄부터 테스트 케이스의 별로 자리 수 N과 N자리 16진수가 주어진다. 1<=N<=100

# 16진수 A부터 F는 대문자로 표시된다.
 
# [출력]

# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

import sys

input = sys.stdin.readline

# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
T = int(input())

num = '123456789'
alpha = 'ABCDEF'
dict = { 'A' : 10, 'B': 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F': 15}

for i in range(T):
    
    num, hexa = input().strip().split(' ')
    answer = []
    
    # print("num, hexa: ", num, hexa)
    
    # hexa를 list화
    hexa = list(hexa)
    
    for j in range(len(hexa)):
        if hexa[j] in alpha:
            hexa[j] = dict[hexa[j]]
        else:
            hexa[j] = int(hexa[j])
    
    for j in range(len(hexa)):
        answer.append(format(hexa[j], '04b'))
    
    answer = ''.join(answer)    
    
    print("#{} {}".format(i+1, answer))

