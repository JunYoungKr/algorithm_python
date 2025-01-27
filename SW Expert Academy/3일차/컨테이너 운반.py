import sys

input = sys.stdin.readline

N = int(input())

coins = [500, 100, 50, 10]

answer = 0

for coin in coins:
    # print(coin)
    answer += N // coin
    N %= coin
    print(N)
    
print(answer)