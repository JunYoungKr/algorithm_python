import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))

result = []
index = 0

queue = list(range(1, N + 1))

while queue:
    index = (index + K - 1) % len(queue)
    
    person = queue.pop(index)
    result.append(person)
    
print("<" + ", ".join(map(str, result)) + ">")
