import sys
input = sys.stdin.readline

# N장의 카드
N = int(input())

card = [i for i in range(1, N+1)]

stack = []

while card:
    # 맨 위에 있는 카드를 버린다.
    stack.append(card.pop(0))
    
    # 그 다음 맨 위에 있는 카드를 맨 아래로 옮긴다.
    if card:
        card.append(card.pop(0))
    
for i in stack:
    print(i, end=' ')