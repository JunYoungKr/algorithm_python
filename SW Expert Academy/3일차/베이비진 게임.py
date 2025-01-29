import sys
input = sys.stdin.readline

# 0~9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 고름

# run : 연속인 숫자가 3개 이상
# triplet : 같은 숫자가 3개 이상

def baby(count, idx):
    if count[idx] == 3:
        return 1
    for i in (idx-2, idx-1, idx):
        if 0 <= i <= 7 and count[i] > 0 and count[i+1] > 0 and count[i+2] > 0:
            return 1
    return 0

# 테스트케이스 T 입력
T = int(input())

for case in range(1, T+1):
    cards = list(map(int, input().split(' ')))
    
    # count1, 2 배열 (빈도수 체크)
    count1 = [0] * 10
    count2 = [0] * 10
    
    ans = 0
    
    for i in range(len(cards)):
        # 짝수인 경우
        if i % 2 == 0:
            count1[cards[i]] += 1
            if baby(count1, cards[i]):
                ans = 1
                break
        else:
            count2[cards[i]] += 1
            if baby(count2, cards[i]):
                ans = 2
                break