def solution(N, number):
    dp = []
    def four_operations(calculated, n1, n2):
        calculated.add(n1*n2)
        calculated.add(n1+n2)
        calculated.add(n1-n2)
        if n1 > 0 and n2 > 0:
            calculated.add(n1//n2)
            
    for cnt in range(1, 9):
        calculated = set()
        calculated.add(int(str(N) * cnt))
        for i in range(len(dp)):
            for n1 in dp[i]:
                for n2 in dp[-i-1]:
                    four_operations(calculated, n1, n2)
                    
        if number in calculated:
            return cnt
        
        dp.append(calculated)
        
    return -1
