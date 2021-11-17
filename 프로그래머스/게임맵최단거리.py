from collections import deque
def solution(maps):
    answer = 0

    DELTAS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    n = len(maps)
    m = len(maps[0])
    distance = [[1e9] * (m) for _ in range(n)]
    dq = deque([(0, 0, 1)])
    distance[0][0] = 1

    while dq:

        x, y, cnt = dq.popleft()
      

        for dx, dy in DELTAS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                distance[nx][ny] = cnt + 1
                maps[nx][ny] = 0
                dq.append((nx, ny, cnt + 1))
    
    return distance[-1][-1] if distance[-1][-1] != 1e9 else -1
                
