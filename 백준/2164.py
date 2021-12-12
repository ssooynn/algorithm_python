from collections import deque

n = int(input())

dq = deque([i for i in range(1, n+1)])
while len(dq) > 1:
    dq.popleft()
    card = dq.popleft()
    dq.append(card)

print(dq[0])