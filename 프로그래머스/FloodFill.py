from collections import deque

def solution(n, m, image):
    answer = 0
    INF = 1e9

    def bfs(x, y, num):
        DX, DY = [1, 0, -1, 0], [0, 1, 0, -1]
        dq = deque([(x, y, 1)])
        total = 1
        while dq:
            x, y, cnt = dq.popleft()
            total = max(cnt, total)
            for dnx, dny in zip(DX, DY):
                nx, ny = x + dnx, y + dny
                if 0 <= nx < n and 0 <= ny < m:
                    if num == image[nx][ny]:
                        image[nx][ny] = INF
                        dq.append((nx, ny, cnt + 1))

        return total

    for i in range(n):
        for j in range(m):
            if image[i][j] != INF:
                bfs(i, j, image[i][j])
                answer += 1

    return answer
