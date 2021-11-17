
n = int(input())
board = []
answer = 1e9
members = [i for i in range(n)]
for _ in range(n):
    board.append(list(map(int, input().split())))

def solution(board, start, index):
    global members
    global answer
    if len(start) > n//2:
        return
    if len(start) == n//2:
        link = []
        for i in members:
            if i not in start:
                link.append(i)
        s_score, l_score = 0, 0
        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                s_score += board[start[i]][start[j]]
                l_score += board[link[i]][link[j]]
        answer = min(abs(s_score - l_score), answer)
        return

    for i in range(index, len(members)):
        start.append(i)
        solution(board, start , i+1)
        start.pop()
    return


solution(board, [], 0)
print(answer)
