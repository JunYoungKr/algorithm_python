import sys
input = sys.stdin.readline

N = input().upper()

# print(N)

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

arr = [0] * 26

for i in N:
    if i in alpha:
        arr[alpha.index(i)] += 1
        
# print("arr: ", arr)

# count = 0

max = max(arr)
# print("max: ", max)

count = 0

if arr.count(max) >= 2:
    print("?")
else:
    print(alpha[arr.index(max)])