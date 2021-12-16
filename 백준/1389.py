from collections import defaultdict
from collections import deque

n, m = map(int, input().split())
link = defaultdict(list)
result = 0
min_val = 1e9

for _ in range(m):
    x, y = map(int, input().split())
    if y not in link[x]:
        link[x].append(y)
    if x not in link[y]:
        link[y].append(x)


def bfs(start):
    global link, n
    answer = 0
    stack = deque([(start, 0)])
    visited = [False]*(n+1)
    visited[start] = True
    while stack:
        tmp, count = stack.popleft()
        answer += count
        for adjs in link[tmp]:
            if visited[adjs] == False:
                visited[adjs] = True
                stack.append((adjs, count+1))
    return answer


for i in range(1, n+1):
    tmp_val = bfs(i)
    if tmp_val < min_val:
        min_val = tmp_val
        result = i

print(result)






