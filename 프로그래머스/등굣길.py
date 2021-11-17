def number_of_cases(i, j, dp):
    if j > 0:
        left = dp[i][j-1]
    else:
        left = 0
    if i > 0:
        upper = dp[i-1][j]
    else:
        upper = 0

    return left + upper

def solution(m, n, puddles):
    
    dp = [[1] * m for _ in range(n)]           
    for y, x in puddles:
        dp[x-1][y-1] = 0
    
    for i in range(0, n):
        for j in range(0, m):
            if [j+1, i+1] in puddles or (i == 0 and j == 0):
                continue
            dp[i][j] = number_of_cases(i, j, dp)
    
    return dp[-1][-1] % 1_000_000_007
