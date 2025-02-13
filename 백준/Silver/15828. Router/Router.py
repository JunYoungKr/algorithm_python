import sys
input = sys.stdin.readline

from collections import deque

# 버퍼의 크기 N
N = int(input())

# 양의 정수 -> 해당하는 번호의 패킷이 입력으로 들어왔다는 것을 의미
# 0 -> 라우터가 패킷 하나를 처리, 즉 queue에서 뺏다는 뜻

queue = deque()

while True:
    num = int(input())
    
    if num == -1:
        break
    
    elif num == 0:
        queue.popleft()
    else:
        queue.append(num)
    
for i in queue:
    print(i, end=' ')