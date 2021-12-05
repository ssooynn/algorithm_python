import sys
from collections import deque
input = sys.stdin.readline
DELTAS = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs():
    dq = deque([(0, 0, 1)])
    visited = [[[0] * 2 for i in range(m)] for i in range(n)]
    visited[0][0][1] = 1
    while dq:
        x, y, w = dq.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]

        for dx, dy in DELTAS:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 1 and w == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    dq.append([nx, ny, 0])

                elif data[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    dq.append([nx, ny, w])
    return -1

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, list(input().strip()))))

print(bfs())