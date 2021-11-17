def check_digonal_bingo(board, N):
    for i in range(N):
        if board[i][i] != 0:
            return 0
    return 1

def y_axis_symmetry(board, N):
    for i in range(N):
        for j in range(N//2):
            board[i][j], board[i][N-j-1] = board[i][N-j-1], board[i][j]
    return board

def solution(board, nums):
    N = len(board)
    num_info = dict()
    get_x, get_y = [0] * N, [0] * N

    for i in range(N):
        for j in range(N):
            num_info[board[i][j]] = (i, j)

    for num in nums:
        x, y = num_info[num]
        get_x[x] += 1
        get_y[y] += 1
        board[x][y] = 0

    return get_x.count(N) + get_y.count(N) + check_digonal_bingo(board, N) + check_digonal_bingo(
        y_axis_symmetry(board, N), N)

