import sys
input = sys.stdin.readline

from collections import deque

# 버퍼의 크기 N
N = int(input())

# 양의 정수 -> 해당하는 번호의 패킷이 입력으로 들어왔다는 것을 의미
# 0 -> 라우터가 패킷 하나를 처리, 즉 queue에서 뺏다는 뜻

queue = deque()

# 버퍼의 크기를 넘치지 않으면서
while True:
    num = int(input())
    
    if num == -1:
        break
    
    # 입력이 0이라면 popleft()
    if num == 0:
        queue.popleft()
    # 
    elif len(queue) < N:
        queue.append(num)
    # print("queue: ", queue)
if queue:
    for i in queue:
        print(i, end=' ')   
else:
    print('empty')