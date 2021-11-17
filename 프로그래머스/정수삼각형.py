def solution(triangle):
    n = len(triangle)
    dp = [triangle[0]]
    
    for i in range(1, n):
        temporary_dp = []
        m = len(triangle[i])
        left, right = 0, 0
        for j in range(m):
            if j - 1 >= 0:
                left = dp[i-1][j-1]
            if j + 1 < m:
                right = dp[i-1][j]
            
            temporary_dp.append((triangle[i][j] + max(left, right)))
            
        dp.append(temporary_dp)
    
    return max(dp[-1])
