from collections import deque
def solution(ground, n, m):
    visited = [[0] * m for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] and not visited[i][j]:
                answer += 1
                dq = deque([(i, j)])
                while dq:
                    x, y = dq.popleft()
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = dx + x, dy + y
                        if 0 <= nx < n and 0 <= ny < m:
                            if ground[nx][ny] and not visited[nx][ny]:
                                dq.append((nx, ny))
                                visited[nx][ny] = 1

    return answer

if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        m, n, num = map(int, input().split())
        ground = [[0] * m for _ in range(n)]
        for _ in range(num):
            x, y = map(int, input().split())
            ground[y][x] = 1
        print("\n", solution(ground, n, m))
