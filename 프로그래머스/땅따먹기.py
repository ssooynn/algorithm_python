def get_visitable_indexes(stepped_index):
    return [i for i in range(4) if i != stepped_index]


def solution(land):
    n = len(land)
    dp = [[0] * 4 for _ in range(n)]

    for k in range(4):
        dp[0][k] = land[0][k]

    for i in range(1, n):
        for j in range(4):
            dp[i][j] = land[i][j] + max([dp[i - 1][index] for index in get_visitable_indexes(j)])

    return max(dp[-1])

