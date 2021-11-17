def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def bfs(start):
        stack = [start]
        while stack:
            node = stack.pop()
            for v in range(n):
                if v != node and computers[node][v] and visited[v] == 0:
                    visited[v] = 1
                    stack.append(v)
        return
    
    for i in range(n):
        if visited[i] == 0:
            bfs(i)
            #print(visited)
            answer += 1
                
    return answer